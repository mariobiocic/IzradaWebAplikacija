#!C:/Users/mario/AppData/Local/Programs/Python/Python313/python.exe

import cgi, mysql.connector, hashlib
from http import cookies
import uuid

print("Content-Type: text/html; charset=UTF-8\n")

params = cgi.FieldStorage()
name = params.getfirst("name", "").strip()
email = params.getfirst("email", "").strip()
password = params.getfirst("password", "")
confirm = params.getfirst("confirm", "")

errors = []

if not name:
    errors.append("Ime nije uneseno.")
if not email:
    errors.append("Email nije unesen.")
if not password:
    errors.append("Lozinka nije unesena.")
if password != confirm:
    errors.append("Lozinke se ne podudaraju.")

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="odabir_predmeta"
)
cursor = db.cursor()

if not errors:
    cursor.execute("SELECT * FROM users WHERE email=%s", (email,))
    if cursor.fetchone():
        errors.append("Email je već zauzet.")

if not errors:
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    cursor.execute('INSERT INTO users (name, email, password_hash) VALUES (%s, %s, %s)', (name, email, password_hash))
    db.commit()
    cursor.close()
    db.close()

    # ISPRAVNO: HTML sadržaj se **uvijek** ispisuje
    print("""<!DOCTYPE html>
    <html><head><title>Registracija</title></head><body>
    <h2>Registracija uspješna!</h2>
    <p><a href="login.py">Prijavi se ovdje</a></p>
    </body></html>
    """)
    exit()

print("<html><head><title>Registracija</title></head><body>")

if errors:
    print("<ul style='color:red;'>")
    for error in errors:
        print(f"<li>{error}</li>")
    print("</ul>")

print(f"""<form method="POST">
    Ime: <input type="text" name="name" value="{name}"><br>
    Email: <input type="email" name="email" value="{email}"><br>
    Lozinka: <input type="password" name="password"><br>
    Potvrdi lozinku: <input type="password" name="confirm"><br>
    <input type="submit" value="Registriraj se">
</form>
<p>Vec imate racun? <a href="login.py">Prijava</a></p>
</body></html>
""")