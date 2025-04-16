#!C:\Users\mario\AppData\Local\Programs\Python\Python313\python.exe



import os, cgi
from http import cookies



articles ={ 1 : {"name":"CPU", "price" : 400 },
            2 : {"name":"RAM", "price" : 200},
            3 : {"name":"GPU", "price" : 300},
            4 : {"name":"HDD", "price" : 250},
            5 : {"name":"DVD", "price" : 4150}
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

def ispis():
    print('''<h3>Postavljeni Cookie: </h3> <ul>''')
    for key in all_cookies_object:
        print(f"""<li>{key} : {all_cookies_object[key].value}</li> <br>""")
    print('''</ul>''')    


params=cgi.FieldStorage()
cookies_string=os.environ.get('HTTP_COOKIE','')
all_cookies_object=cookies.SimpleCookie(cookies_string)

start_html()
ispis()
end_html()

