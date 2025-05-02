#!C:\Users\mario\AppData\Local\Programs\Python\Python313\python.exe

import os, cgi
from http import cookies


params=cgi.FieldStorage()

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
    print('''</body>
    </html>''')


def forma():
    print('''<form method="post" action="">''')
    ispis_predmeta()
    print('''<input type="submit" value="Add"> <br>''')
    print('''<a href="kosarica.py"> Vidi ispis predmeta''')
    print('''</form>''')


def ispis_predmeta():
    for key, data in subjects.items():
        print(f"<input type='checkbox' value='{key}' name='predmeti' > {data['name']} : {data['ects']} <br>")

def create_cookie():
    if "predmeti" in params:
        odabrani=params.getlist("predmeti")
        cookie=cookies.SimpleCookie()
        for key in odabrani:
            if key in subjects:
                cookie[key]=subjects[key]['name']
        print(cookie.output())       


cookies_string=os.environ.get('HTTP_COOKIE','')
all_cookies_object=cookies.SimpleCookie(cookies_string)
create_cookie()
start_html()
forma()
end_html()    