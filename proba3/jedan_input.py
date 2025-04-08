#!C:\Users\mario\AppData\Local\Programs\Python\Python313\python.exe

import cgi, os
from http import cookies


    
def create_cookie():
    if "tekst" in params:
        tekst=params.getvalue("tekst")
        if tekst:
            cookie=cookies.SimpleCookie()
            cookie[tekst]=tekst
            print(cookie.output())

def html_start():
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

def html_end():
    print('''
    </body>
    </html>
    ''')

def forma():
    print('''
    <form method="post" action="">
        <input type="text" name="tekst">
        <br>
        <input type="submit" value="postavi cookie">
    </form>
    ''') 

def je_li_postoji():
        if "tekst" in params:
            tekst=params.getvalue("tekst")
            if tekst and tekst in all_cookies_object:
                print(f"<p>Cookie {tekst} je vec postavljen.</p>")
            else:
                print(f"<p>Cookie {tekst} nije postavljen. Biti ce dodan.</p>")    
        return " "

def ispis():
    print("<h3>Postojeci cookei: </h3><ul>")
    for k in all_cookies_object:
        print(f"<li>Cookie: {k} : {all_cookies_object[k].value} </li>")
    print("</ul>")    

params=cgi.FieldStorage()
create_cookie()
cookies_string=os.environ.get('HTTP_COOKIE','')
all_cookies_object=cookies.SimpleCookie(cookies_string)


html_start()
forma()
je_li_postoji()
ispis()
html_end()    