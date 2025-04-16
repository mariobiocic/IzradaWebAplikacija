#!C:\Users\mario\AppData\Local\Programs\Python\Python313\python.exe

import os, cgi
from http import cookies




subjects = {
    'ip' : { 'name' : 'Introduction' , 'year' : 1, 'ects' : 6 },
    'c1' : { 'name' : 'Calculus1' , 'year' : 1, 'ects' : 7 },
    'cu' : { 'name' : 'Computer usage' , 'year' : 1, 'ects' : 5 },
    'dmt' : { 'name' : 'Digital and microprocessor technology', 'year' : 1, 'ects' : 6 },
    'db' : { 'name' : 'Databases' , 'year' : 2, 'ects' : 6 },
    'c2' : { 'name' : 'Calculus2' , 'year' : 2, 'ects' : 7 },
    'dsa' : { 'name' : 'Data structures and alghoritms' , 'year' : 2, 'ects' : 5 },
    'ca' : { 'name' : 'Computer architecture', 'year' : 2, 'ects' : 6 },
    'isd' : { 'name' : 'Information system sdesign' , 'year' : 3, 'ects' : 5 },
    'c3' : { 'name' : 'Calculus3' , 'year' : 3, 'ects' : 7 },
    'sa' : { 'name' : 'Server Architecture' , 'year' : 3, 'ects' : 6 },
    'cds' : { 'name' : 'Computer and data security', 'year' : 3, 'ects' : 6 }
    }


def create_cookie():
    if "predmet" in params:
        odabrani=params.getlist("predmet")
        cookie=cookies.SimpleCookie()
        for key in odabrani:
            if key in subjects:
                cookie[key]=subjects[key]['name']
        print(cookie.output())

def je_li_postoji():
    if "predmet" in params:
        odabrani=params.getlist("predmet")
        for key in odabrani:
            naziv_pr=subjects[key]['name'] if key in subjects else 'Nepoznat predmet'
            if key in all_cookies_object:
                print(f"<p> Cookie {naziv_pr} ({key}) je vec postavljen.</p>")
            else:    
                print(f"<p>Cookie {naziv_pr} ({key}) nije dodan, sada ce biti postavljen.</p>")
    return ""

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
    predmeti()
    print('''<input type="submit" value="Postavi cookie">''')
    print('''<br>''')
    print('<a href="postojeci_cookie.py"><button type="button">Prikazi sve cookieje</button></a>')
    print('''</form>''')  

def predmeti():
    for key, data in subjects.items():
        print(f"{data['name']} ")
        print(f'<input type="checkbox" name="predmet" value="{key}"> <br>')


params=cgi.FieldStorage()


cookies_string=os.environ.get('HTTP_COOKIE','')
all_cookies_object=cookies.SimpleCookie(cookies_string)


create_cookie()
start_html()
forma()
je_li_postoji()
end_html()      