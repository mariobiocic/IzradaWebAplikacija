#!C:/Users/mario/AppData/Local/Programs/Python/Python313/python.exe

import cgi, mysql.connector, hashlib
from http import cookies
import uuid

params = cgi.FieldStorage()
email = params.getfirst("email", "").strip()
password = params.getfirst("password", "")

errors = []
session_id = None

# Connect to the database
try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="odabir_predmeta"
    )
    cursor = db.cursor()
except mysql.connector.Error as err:
    print("Content-Type: text/html; charset=UTF-8\n")
    print(f"<p>Greška pri spajanju na bazu: {err}</p>")
    exit()

if not email or not password:
    errors.append("Molimo unesite email i lozinku.")
else:
    # Fetch user from the database
    cursor.execute("SELECT id, name, email, password_hash FROM users WHERE email=%s", (email,))
    user = cursor.fetchone()

    if user:
        user_id, name, stored_email, stored_password_hash = user
        if hashlib.sha256(password.encode()).hexdigest() == stored_password_hash:
            session_id = str(uuid.uuid4())
            cursor.execute("INSERT INTO sesije2 (session_id, user_id) VALUES (%s, %s)", (session_id, user_id))
            db.commit()
        else:
            errors.append("Kriva lozinka.")
    else:
        errors.append("Korisnik s tim emailom ne postoji.")

cursor.close()
db.close()

# Sada odlučujemo što ispisujemo
if not errors and session_id:
    # ISPRAVNO: Sve zaglavlje odjednom
    print(f"Content-Type: text/html; charset=UTF-8")
    print(f"Set-Cookie: session_id={session_id}; path=/")
    print()
    print(f"""
    <html><head><title>Prijava</title></head><body>
    <p>Prijavljeni ste kao {name}. <a href='db.py'>Idite na odabir predmeta</a></p>
    </body></html>
    """)
else:
    # Ispis u slučaju greške
    print("Content-Type: text/html; charset=UTF-8\n")
    print("""
    <html><head><title>Prijava</title></head><body>
    <h1>Prijava</h1>
    <ul style="color:red;">
    """)
    for e in errors:
        print(f"<li>{e}</li>")
    print("</ul>")
    print("""
    <form method="POST">
        Email: <input type="email" name="email"><br>
        Lozinka: <input type="password" name="password"><br>
        <input type="submit" value="Prijavi se">
    </form>
    <p>Nemate racun? <a href="register.py">Registracija</a></p>
    </body></html>
    """)
