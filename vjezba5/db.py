#!C:/Users/mario/AppData/Local/Programs/Python/Python313/python.exe

import os
import cgi
import mysql.connector

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

# Spajanje na bazu i stvaranje kursora
db = connect_db()
cursor = db.cursor(dictionary=True)

# Glavni HTML start
def html_start(title="Popis predmeta"):
    print(f"<!DOCTYPE html><html><head><meta charset='UTF-8'><title>{title}</title></head><body>")

# HTML završetak
def html_end():
    print("</body></html>")

# Dohvaćanje i ispis predmeta
def ispisi_subjects():
    user_id = 1  # Ovo ćemo kasnije dohvatiti iz cookieja
    
    cursor.execute("SELECT * FROM subjects")
    subjects = cursor.fetchall()

    # Dohvati postojeće statuse korisnika
    cursor.execute("SELECT subject_id, status FROM subject_status WHERE user_id = %s", (user_id,))
    status_map = {row['subject_id']: row['status'] for row in cursor.fetchall()}

    # HTML forma za odabir statusa
    print("<form method='POST' action='spremi_status.py'>")
    print("<table border='1'>")
    print("<tr><th>ID</th><th>Kod</th><th>Ime</th><th>Bodovi</th><th>Godina</th><th>Status</th></tr>")

    for subject in subjects:
        subject_id = subject['id']
        current_status = status_map.get(subject_id, "not selected")

        print(f"""
        <tr>
            <td>{subject['id']}</td>
            <td>{subject['kod']}</td>
            <td>{subject['ime']}</td>
            <td>{subject['bodovi']}</td>
            <td>{subject['godina']}</td>
            <td>
                <input type="radio" name="status_{subject_id}" value="enrolled" {"checked" if current_status == "enrolled" else ""}> Upisan
                <input type="radio" name="status_{subject_id}" value="passed" {"checked" if current_status == "passed" else ""}> Položen
                <input type="radio" name="status_{subject_id}" value="not selected" {"checked" if current_status == "not selected" else ""}> Nije odabrano
            </td>
        </tr>
        """)

    print("</table>")
    print("<br><input type='submit' value='Spremi odabir'>")
    print("</form>")

    # Gumb za odjavu
    print("""
    <form action="logout.py" method="get">
    <br>
        <button type="submit">Odjava</button>
    </form>
    """)

    # Gumb za promjenu lozinke
    print("""
    <form action="change.py" method="get">
    <br>
        <button type="submit">Promijeni lozinku</button>
    </form>
    """)

# Glavni program
html_start()
ispisi_subjects()
html_end()

# Zatvaranje baze
cursor.close()
db.close()
