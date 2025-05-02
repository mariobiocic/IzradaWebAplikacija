#!C:\Users\mario\AppData\Local\Programs\Python\Python313\python.exe

import os, cgi
from http import cookies

params=cgi.FieldStorage()
cookies_string=os.environ.get('HTTP_COOKIE','')
all_cookies_object=cookies.SimpleCookie(cookies_string)

def start_html():
    print('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>''')

def end_html():
    print('''
    </body>
    </html>
    ''')


def forma():
    print('''<form method="post" action="">''')
    print('''<br> Key: <input type="text" name="key"> <br>''')
    print('''<br> Value: <input type="text" name="val"> <br>''')
    print('''<input type="submit" value="Postavi">''')
    print('''</form>''')

def create_cookie():
    if "key" in params and "val" in params:
        klj=params.getvalue("key")
        vri=params.getvalue("val")
        cookie=cookies.SimpleCookie()
        cookie[klj]=vri
        print(cookie.output())

def ispis():

    print('''<h3>Postojeci cookie: </h3> <ul>''')
    for key in all_cookies_object:
        print(f"<li> {key} : {all_cookies_object[key].value} </li><br>")
    print('''</ul>''')



create_cookie()
start_html()
forma()
print('''<br>''')
ispis()
end_html()