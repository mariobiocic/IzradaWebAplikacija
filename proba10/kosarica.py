#!C:\Users\mario\AppData\Local\Programs\Python\Python313\python.exe

import os, cgi
from http import cookies


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

def ispis_imena():
    print('''<h3>Odabrani</h3> <ul> <br>''')
    for key in all_cookies_object:
        print(f"<li>{all_cookies_object[key].value}</li><br>")
    print('''</ul>''')    








start_html()
ispis_imena()
print('''<br> <a href="imena.py">Imena''')
end_html()