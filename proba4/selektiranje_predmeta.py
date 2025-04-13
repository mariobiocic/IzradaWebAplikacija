#!C:\Users\mario\AppData\Local\Programs\Python\Python313\python.exe

import os, cgi
from http import cookies

params = cgi.FieldStorage()

subjects = {
    1: "Baze Podataka",
    2: "Programiranje u C#",
    3: "Python",
    4: "Programiranje u Javi",
    5: "Izrada Web Aplikacija"
}

def create_cookie():
    if "predmet" in params:
        vrijednosti = params.getlist("predmet")
        imena = [subjects[int(v)] for v in vrijednosti if v.isdigit() and int(v) in subjects]
        if imena:
            cookie = cookies.SimpleCookie()
            cookie["predmet"] = " | ".join(imena)  
            print(cookie.output()) 

def start_html():
    print('''
    <!DOCTYPE html>
    <html lang="hr">
    <head>
    <meta charset="UTF-8">
    <title>Odabir predmeta</title>
    </head>
    <body>
    ''')

def end_html():
    print('''
    </body>
    </html>
    ''')

def forma():
    print('<form method="post" action="">')
    ispis_predmeta()
    print('<input type="submit" value="Posalji">')
    print('</form>')

def ispis_predmeta():
    for k, v in subjects.items():
        print(f'<input type="checkbox" name="predmet" value="{k}"> {v}<br>')

def ispisi_odabire():
    print('''<h3> Setted-Cookies: </h3> <ul>''')
    for key in all_cookies_object:
        print(f"<li>{all_cookies_object[key].value}</li>")
    print('''</ul>''')        

cookies_string=os.environ.get('HTTP_COOKIE','')
all_cookies_object=cookies.SimpleCookie(cookies_string)
create_cookie()
start_html()
forma()
ispisi_odabire()
end_html()
