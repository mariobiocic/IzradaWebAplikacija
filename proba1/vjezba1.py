#!C:\Users\mario\AppData\Local\Programs\Python\Python313\python.exe

import os, cgi
from http import cookies

print("Content-Type: text/html")

params = cgi.FieldStorage()

def start_html():
    print('''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    ''')

def end_html():
    print('''      
</body>
</html>
''')

def create_cookie():
    if "key" in params and "value" in params:
        key_input = params.getvalue("key")
        value_input = params.getvalue("value")
        cookie = cookies.SimpleCookie()
        cookie[key_input] = value_input
        print(cookie.output())

def forma():
    print('''
    <form method="post" action="">
        <label>Kljuc: </label>
        <input type="text" name="key">
        <br>
        <label>Vrijednost: </label>
        <input type="text" name="value">
        <br><br>
        <input type="submit" value="Postavi cookie">
    </form>
    ''')

# Postavi cookie ako forma ima vrijednosti
create_cookie()

# Prikupi sve cookieje od korisnika
cookies_string = os.environ.get('HTTP_COOKIE','')
all_cookies_object = cookies.SimpleCookie(cookies_string)

# HTML ispis
start_html()
forma()

# Prikaži cookieje
print("<h3>Postojeci cookieji:</h3><ul>")
for k in all_cookies_object:
    print(f"<li>{k} = {all_cookies_object[k].value}</li>")
print("</ul>")

end_html()
