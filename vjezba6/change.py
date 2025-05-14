#!C:/Users/mario/AppData/Local/Programs/Python/Python313/python.exe
import cgi, os, mysql.connector, hashlib
from http import cookies

print("Content-Type: text/html; charset=UTF-8\n")

# Funkcija za ispis forme
def ispisi_formu(errors=[]):
    print("""
    <html><head><title>Promjena lozinke</title></head><body>
    <h1>Promjena lozinke</h1>
    """)
    if errors:
        print("<ul style='color:red;'>")
        for e in errors:
            print(f"<li>{e}</li>")
        print("</ul>")
    
    print("""
    <form method="POST">
        Stara lozinka: <input type="password" name="old_password"><br>
        Nova lozinka: <input type="password" name="new_password"><br>
        Potvrdi novu lozinku: <input type="password" name="confirm_password"><br>
        <input type="submit" value="Promijeni lozinku">
    </form>
    </body></html>
    """)

# Provjera je li POST ili GET
request_method = os.environ.get('REQUEST_METHOD', 'GET')

if request_method == 'GET':
    ispisi_formu()
    exit()

# Ako je POST, obradi podatke
params = cgi.FieldStorage()
old_password = params.getfirst("old_password", "")
new_password = params.getfirst("new_password", "")
confirm_password = params.getfirst("confirm_password", "")

errors = []

# Validacija unosa
if not old_password or not new_password or not confirm_password:
    errors.append("Molimo unesite staru i novu lozinku.")
if new_password != confirm_password:
    errors.append("Nove lozinke se ne podudaraju.")

# Provjera session_id iz kolačića
cookies_string = os.environ.get('HTTP_COOKIE', '')
all_cookies = cookies.SimpleCookie(cookies_string)

if "session_id" in all_cookies:
    session_id = all_cookies["session_id"].value

    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="odabir_predmeta"
        )
        cursor = db.cursor()

        cursor.execute("SELECT user_id FROM sesije2 WHERE session_id=%s", (session_id,))
        result = cursor.fetchone()
        if result:
            user_id = result[0]
        else:
            errors.append("Sesija nije ispravna.")

        if not errors:
            cursor.execute("SELECT password_hash FROM users WHERE id=%s", (user_id,))
            result = cursor.fetchone()
            if result and hashlib.sha256(old_password.encode()).hexdigest() == result[0]:
                new_hash = hashlib.sha256(new_password.encode()).hexdigest()
                cursor.execute("UPDATE users SET password_hash=%s WHERE id=%s", (new_hash, user_id))
                db.commit()
                cursor.close()
                db.close()
                print("""
                <html><head><title>Promjena lozinke</title></head><body>
                <h1 style="color:green;">Lozinka uspješno promijenjena!</h1>
                <p><a href='db.py'>Povratak na početnu</a></p>
                </body></html>
                """)
                exit()
            else:
                errors.append("Stara lozinka nije ispravna.")
    except mysql.connector.Error as err:
        errors.append(f"Greška pri radu s bazom podataka: {err}")
else:
    errors.append("Niste prijavljeni.")

# Ako ima grešaka, ponovno prikaži formu s greškama
ispisi_formu(errors)
