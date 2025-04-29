#!C:\Users\mario\AppData\Local\Programs\Python\Python313\python.exe

import os, cgi
from http import cookies

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
        
year_names = {
        1 : '1st Year',
        2 : '2nd Year',
        3 : '3rd Year'
    }

year_ids = {
        '1st Year' : 1,
        '2nd Year' : 2,
        '3rd Year' : 3
}

status_names = {
    'not' : 'Not Selected',
    'enr' : 'Enrolled',
    'pass' : 'Passed',
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
    <body>
    ''')

def end_html():
    print('''
    </body>
    </html>
    ''')

def forma():
    print('''<form method="post" action="">''')

    ispis_predmeta()

    print('''<input type="submit" value="postavi cookie">''')    
    print('''</form>''')    

def ispis_predmeta():
    for key, data in subjects.items():
        print(f'<input type="checkbox" name="predmet" value="{key}"> {data['name']} : {data['ects']} <br>')

def create_cookie():
    if "predmet" in params:
       odabrani=params.getlist("predmet") 
       cookie=cookies.SimpleCookie()
       for key in odabrani:
         if key in subjects:
            cookie[key]=subjects[key]['ects'] 
       print(cookie.output())       

def ispis():

    print('''<h3>Svi cookei:</h3> <ul>''')
    for key in all_cookies_object:
        print(f"<li>{key} : {all_cookies_object[key].value}</li>")
    print('''</ul>''')


def suma():
    suma=0
    for key in all_cookies_object:
        suma=suma+int(all_cookies_object[key].value)

    print(f"<p> Suma odabranih je: {suma} </p>")    



params=cgi.FieldStorage()
cookies_string=os.environ.get('HTTP_COOKIE','')
all_cookies_object=cookies.SimpleCookie(cookies_string)
create_cookie()
start_html()
forma()
ispis()
suma()
end_html()    
print(params)    