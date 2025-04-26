#!C:/Users/mario/AppData/Local/Programs/Python/Python313/python.exe

import os, cgi
from http import cookies
import mysql.connector
import predmeti

print("Content-Type: text/html; charset=UTF-8")
print()


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="odabir_predmeta"
)
cursor = db.cursor()


params = cgi.FieldStorage()
cookies_string = os.environ.get('HTTP_COOKIE', '')
all_cookies = cookies.SimpleCookie(cookies_string)

if "session_id" in all_cookies:
    session_id = all_cookies["session_id"].value
else:
    session_id = "user1"
    print("Set-Cookie: session_id=user1; path=/")


def get_status(subject_id):
    cursor.execute("SELECT status FROM sesije WHERE session_id=%s AND subject_id=%s", (session_id, subject_id))
    result = cursor.fetchone() #rez od preth
    return result[0] if result else 'not'


def spremi_odabire():
    for subject_id in predmeti.subjects:
        value = params.getfirst(subject_id)
        if value in predmeti.status_names:
            cursor.execute("""
                INSERT INTO sesije (session_id, subject_id, status)
                VALUES (%s, %s, %s)
                ON DUPLICATE KEY UPDATE status=%s
            """, (session_id, subject_id, value, value))
    db.commit()


def start_html():
    print("""
    <!DOCTYPE html>
    <html><head><meta charset="UTF-8"><title>Predmeti</title></head><body>
    <h1>Odabir predmeta</h1>
    """)

def end_html():
    print("</body></html>")

def forma():
    print('<form method="POST" action="">')
    for year, label in predmeti.year_names.items():
        print(f'<button type="submit" name="year" value="{year}">{label}</button>')
    print("""
    <table border="1">
        <tr><th>Predmet</th><th>ECTS</th><th>Status</th></tr>
    """)

def forma_kraj():
    print("</table></form>")


def ispisi_predmet_sa_odabirom(subject_id, subject_data):
    current = get_status(subject_id)
    print(f"""
    <tr>
        <td>{subject_data['name']}</td>
        <td>{subject_data['ects']}</td>
        <td>
            {"".join([
                f'<input type="radio" name="{subject_id}" value="{k}" {"checked" if current == k else ""}><label>{v}</label>'
                for k, v in predmeti.status_names.items()
            ])}
        </td>
    </tr>
    """)


def ispisi_predmete_godine(godina):
    for subject_id, subject_data in predmeti.subjects.items():
        if subject_data['year'] == godina:
            ispisi_predmet_sa_odabirom(subject_id, subject_data)

def ispisi_upisni_listu():
    for subject_id, subject_data in predmeti.subjects.items():
        status = get_status(subject_id)
        print(f"<tr><td>{subject_data['name']}</td><td>{subject_data['ects']}</td><td>{predmeti.status_names.get(status, 'Not selected')}</td></tr>")


def display_subjects(year):
    if year == 4:
        ispisi_upisni_listu()
    else:
        ispisi_predmete_godine(year)


def zbroj_ects():
    suma = 0
    for subject_id, subject_data in predmeti.subjects.items():
        if get_status(subject_id) == 'pass':
            suma += subject_data['ects']
    print(f"<p>Zbroj polozenih ECTS bodova: {suma}</p>")


if os.environ.get("REQUEST_METHOD") == "POST":
    spremi_odabire()

selected_year = int(params.getfirst("year", "1"))

start_html()
forma()
display_subjects(selected_year)
forma_kraj()
zbroj_ects()
end_html()

cursor.close()
db.close()
