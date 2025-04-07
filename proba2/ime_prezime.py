#!C:\Users\mario\AppData\Local\Programs\Python\Python313\python.exe

import cgi
from http import cookies

params = cgi.FieldStorage()

def create_cookie():
    if "ime" in params and "prezime" in params:
        ime = params.getvalue("ime")
        prezime = params.getvalue("prezime")
        cookie = cookies.SimpleCookie()
        cookie["ime"] = ime
        cookie["prezime"] = prezime
        print(cookie.output())
        print("Location: ispis.py\n")
        exit()

create_cookie()

print("Content-Type: text/html\n")
print('''
<!DOCTYPE html>
<html>
<body>
    <form method="post" action="ime_prezime.py">
        <label>Ime:</label>
        <input type="text" name="ime"><br>
        <label>Prezime:</label>
        <input type="text" name="prezime"><br>
        <input type="submit" value="Postavi">
    </form>
</body>
</html>
''')
