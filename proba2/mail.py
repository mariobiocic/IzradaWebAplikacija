#!C:\Users\mario\AppData\Local\Programs\Python\Python313\python.exe

import cgi
from http import cookies

params = cgi.FieldStorage()

def create_cookie():
    if "mail" in params:
        mail = params.getvalue("mail")
        cookie = cookies.SimpleCookie()
        cookie["mail"] = mail
        print(cookie.output())
        print("Location: ispis.py\n")
        exit()

create_cookie()

print("Content-Type: text/html\n")
print('''
<!DOCTYPE html>
<html>
<body>
    <form method="post" action="mail.py">
        <label>Mail:</label>
        <input type="text" name="mail"><br>
        <input type="submit" value="Postavi">
    </form>
</body>
</html>
''')
