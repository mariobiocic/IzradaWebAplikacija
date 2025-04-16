#!C:\Users\mario\AppData\Local\Programs\Python\Python313\python.exe

import os, cgi
from http import cookies


articles ={ 1 : {"name":"CPU", "price" : 400 },
            2 : {"name":"RAM", "price" : 200},
            3 : {"name":"GPU", "price" : 300},
            4 : {"name":"HDD", "price" : 250},
            5 : {"name":"DVD", "price" : 4150}
            }


def create_cookie():
   if "artikl" in params:
        artikl = params.getlist("artikl")
        cookie = cookies.SimpleCookie()
        for key in artikl:
            if int(key) in articles:
                naziv = articles[int(key)]["name"]
                cijena = articles[int(key)]["price"]
                cookie[key] = f"{naziv}:{cijena}"
        for morsel in cookie.values():
            print(f"Set-Cookie: {morsel.OutputString()}") 

              

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
    art()
    print('''<input type="submit" value="Postavi Cookie">''')
    print('''<br> <a href="kosarica.py"> <button type="button">Provjeri sumu odabranih artikala''')
    print('''</form>''')

def art():
    for key, data in articles.items():
        print(f"""<input type="checkbox" name="artikl" value="{key}">{data['name']} <br>""")

params=cgi.FieldStorage()
cookies_string=os.environ.get('HTTP_COOKIE','')
all_cookies_object=cookies.SimpleCookie(cookies_string)
create_cookie()
start_html()
forma()
end_html()   