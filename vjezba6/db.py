#!C:/Users/mario/AppData/Local/Programs/Python/Python313/python.exe

import os
import cgi
import mysql.connector

print("Content-Type: text/html; charset=UTF-8\n")

db_config = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "odabir_predmeta"
}

def connect_db():
    try:
        return mysql.connector.connect(**db_config)
    except mysql.connector.Error as err:
        print(f"<p>Greška pri povezivanju na bazu: {err}</p>")
        exit()

db = connect_db()
cursor = db.cursor(dictionary=True)

def html_start(title="Popis predmeta"):
    print(f"<!DOCTYPE html><html><head><meta charset='UTF-8'><title>{title}</title></head><body>")

def html_end():
    print("</body></html>")

def ispisi_subjects():
    user_id = 1  # Ovo ćemo kasnije dohvatiti iz cookieja

    cursor.execute("SELECT * FROM subjects")
    subjects = cursor.fetchall()

    # Dohvati statuse studenta iz tablice upisni_list
    cursor.execute("SELECT id_predmeta, status FROM upisni_list WHERE id_studenta = %s", (user_id,))
    status_map = {row['id_predmeta']: row['status'] for row in cursor.fetchall()}

    print("<form method='POST' action='spremi_status.py'>")
    print("<table border='1'>")
    print("<tr><th>ID</th><th>Kod</th><th>Ime</th><th>Bodovi</th><th>Godina</th><th>Status</th></tr>")

    for subject in subjects:
        subject_id = subject['id']
        current_status = status_map.get(subject_id, "not selected")  # Zadana vrijednost

        print(f"""
        <tr>
            <td>{subject['id']}</td>
            <td>{subject['kod']}</td>
            <td>{subject['ime']}</td>
            <td>{subject['bodovi']}</td>
            <td>{subject['godina']}</td>
            <td>
                <input type="radio" name="status_{subject_id}" value="enr" {"checked" if current_status == "enr" else ""}> Upisan
                <input type="radio" name="status_{subject_id}" value="pass" {"checked" if current_status == "pass" else ""}> Polozen
                <input type="radio" name="status_{subject_id}" value="not selected" {"checked" if current_status == "not selected" else ""}> Nije odabrano
            </td>
        </tr>
        """)

    print("</table>")
    print("<br><input type='submit' value='Spremi odabir'>")
    print("</form>")

    print("""
    <form action="logout.py" method="get">
        <br><button type="submit">Odjava</button>
    </form>
    """)

    print("""
    <form action="change.py" method="get">
        <br><button type="submit">Promijeni lozinku</button>
    </form>
    """)

html_start()
ispisi_subjects()
html_end()

cursor.close()
db.close()