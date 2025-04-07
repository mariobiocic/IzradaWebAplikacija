#!C:\Users\mario\AppData\Local\Programs\Python\Python313\python.exe

import cgi
from http import cookies

params = cgi.FieldStorage()

def create_cookie():
    if "status" in params:
        status = params.getvalue("status")
        cookie = cookies.SimpleCookie()
        cookie["status"] = status
        print(cookie.output())
        print("Location: ispis.py\n")
        exit()

create_cookie()

print("Content-Type: text/html\n")
print('''
<!DOCTYPE html>
<html>
<body>
    <form method="post" action="status.py">
        <label>Status studenta:</label><br>
        <input type="radio" id="redovni" name="status" value="redovni">
        <label for="redovni">Redovni</label><br>
        <input type="radio" id="izvanredni" name="status" value="izvanredni">
        <label for="izvanredni">Izvanredni</label><br><br>
        <input type="submit" value="Postavi">
    </form>
</body>
</html>
''')
