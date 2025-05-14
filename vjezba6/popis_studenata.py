#!C:/Users/mario/AppData/Local/Programs/Python/Python313/python.exe

import os
import mysql.connector
import http.cookies

def dohvati_korisnika_iz_sesije():
    cookies_string = os.environ.get('HTTP_COOKIE', '')
    all_cookies = http.cookies.SimpleCookie(cookies_string)
    session_id = all_cookies.get("session_id").value if "session_id" in all_cookies else None

    if not session_id:
        return None

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="odabir_predmeta"
    )
    cursor = conn.cursor(dictionary=True)

    # Dohvati ID i ulogu korisnika
    cursor.execute("""
        SELECT users.id, users.uloga 
        FROM users 
        JOIN sesije2 ON users.id = sesije2.user_id 
        WHERE sesije2.session_id = %s
    """, (session_id,))
    
    result = cursor.fetchone()
    cursor.close()
    conn.close()

    return result if result else None

print("Content-Type: text/html; charset=UTF-8\n")

korisnik = dohvati_korisnika_iz_sesije()
if not korisnik or korisnik['uloga'] != 'admin':
    print("<p>Nemate pravo pristupa.</p>")
    exit()

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="odabir_predmeta"
)
cursor = conn.cursor(dictionary=True)

# Dohvaćamo sve studente koji imaju zapise u upisnom listu
cursor.execute("""
    SELECT users.id, users.name, users.email,  
           COALESCE(GROUP_CONCAT(upisni_list.status SEPARATOR ', '), 'not selected') AS status
    FROM users
    JOIN upisni_list ON users.id = upisni_list.id_studenta  
    WHERE users.uloga = 'student'
    GROUP BY users.id, users.name, users.email
    ORDER BY users.id;
""")
studenti = cursor.fetchall()

print("<h2>Popis studenata na upisnom listu</h2><ul>")

if studenti:  # Provjera jesu li pronađeni studenti
    for s in studenti:
        status_display = s["status"]
        print(f'<li>{s["name"]} ({s["email"]}) - <a href="upisni_list_student.py?id={s["id"]}">{status_display}</a></li>')
else:
    print("<p>Nema studenata na upisnom listu.</p>")  # Ako je lista prazna, ispisuje se poruka

print("</ul>")

# **Dodana opcija za odjavu na dnu stranice**
print("""
<form action="logout.py" method="get">
    <button type="submit">Odjava</button>
</form>
""")

cursor.close()
conn.close()