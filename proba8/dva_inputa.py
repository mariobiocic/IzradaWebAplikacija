#!C:\Users\mario\AppData\Local\Programs\Python\Python313\python.exe

import os, cgi
from http import cookies

def create_cookie():
    if "key" in params and "value" in params:
        key_input=params.getvalue("key")
        value_input=params.getvalue("value")
        cookie = cookies.SimpleCookie()
        cookie[key_input]=value_input
        print(cookie.output())

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

def forma():
    print('''<form method="post" action="">''') 
    print('''<input type="text" name="key">  ''')
    print('''<input type="text" name="value">  ''')
    print('''<br> <br> <input type="submit" value="Set Cookie">''')
    print('''</form>''')   

def ispis():
    print('''<h3>Postojeci cookie</h3><ul>''')
    for k in all_cookies_object:
        print(f"<li>{k} : {all_cookies_object[k].value}</li>")
    print('''</ul>''')


params=cgi.FieldStorage()
cookies_string=os.environ.get('HTTP_COOKIE','')
all_cookies_object=cookies.SimpleCookie(cookies_string)
create_cookie()
start_html()
forma()
ispis()
end_html()