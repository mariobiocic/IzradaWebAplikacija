#!C:/Users/mario/AppData/Local/Programs/Python/Python313/python.exe

import os
import cgi
import cgitb
import mysql.connector
import http.cookies

cgitb.enable()  # Omogućava prikaz grešaka u pregledniku

# HTTP zaglavlje
print("Content-Type: text/html; charset=UTF-8\n")

# Postavke baze podataka
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "odabir_predmeta"
}

# Funkcija za povezivanje na bazu podataka
def connect_db():
    try:
        return mysql.connector.connect(**db_config)
    except mysql.connector.Error as err:
        print(f"<p>Greška pri povezivanju na bazu: {err}</p>")
        exit()

# Funkcija za dohvat korisničkog ID-a iz baze na temelju session_id-a
def get_user_id(session_id):
    cursor.execute("SELECT user_id FROM sesije2 WHERE session_id=%s", (session_id,))
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        print("Location: login.py\n")
        print()  # Prekinuti ispis kako bi preusmjerenje bilo izvršeno
        exit()

# Spajanje na bazu podataka
db = connect_db()
cursor = db.cursor()

# Dohvaćanje session_id-a iz kolačića
cookies_string = os.environ.get('HTTP_COOKIE', '')
all_cookies = http.cookies.SimpleCookie(cookies_string)
session_id = all_cookies.get("session_id").value if "session_id" in all_cookies else None

if not session_id:
    print("Location: login.py\n")
    print()
    exit()

# Dohvaćanje user_id-a na temelju session_id-a
user_id = get_user_id(session_id)

# Dohvati podatke iz forme
form = cgi.FieldStorage()

# Provjera ima li podataka
if not form.list:
    print("<p>Greška: Nisu poslani nikakvi podaci.</p>")
else:
    for field in form.list:
        if field.name.startswith("status_"):
            subject_id = int(field.name.split("_")[1])
            status = field.value

            # Provjeri postoji li već zapis za tog korisnika i predmet
            cursor.execute("SELECT id FROM subject_status WHERE user_id = %s AND subject_id = %s", (user_id, subject_id))
            existing = cursor.fetchone()

            if existing:
                # Ažuriranje postojećeg zapisa
                cursor.execute("UPDATE subject_status SET status = %s WHERE id = %s", (status, existing[0]))
            else:
                # Umetanje novog zapisa
                cursor.execute("INSERT INTO subject_status (user_id, subject_id, status) VALUES (%s, %s, %s)",
                               (user_id, subject_id, status))

    db.commit()

    # Nakon spremanja
    print("""
    <!DOCTYPE html>
    <html lang="hr">
    <head>
        <meta charset="UTF-8">
        <title>Status spremljen</title>
    </head>
    <body>
        <h2>Statusi su uspjesno spremljeni!</h2>
        <a href="db.py">Povratak na popis predmeta</a>
    </body>
    </html>
    """)

# Zatvaranje baze
cursor.close()
db.close()