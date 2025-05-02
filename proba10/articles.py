#!C:\Users\mario\AppData\Local\Programs\Python\Python313\python.exe

import os, cgi
from http import cookies

articles={1 :{"name":"CPU", "price":470},
        2 :{"name":"GPU", "price":200},
        3 :{"name":"RAM", "price":100},
        4 :{"name":"HDD", "price":300}
        }


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
    print('''</body>
    </html>''')


def forma():
    print('''<form method="post" action="">''')
    ispis_artikla()
    print('''<input type="submit" value="Add"> <br>''')
    print('''</form>''')


def ispis_artikla():
    for key, data in articles.items():
        print(f"<input type='checkbox' value='{key}' name='arti' > {data['name']} - {data['price']} <br>")


def create_cookie():
    if "arti" in params:
        odabrani=params.getlist("arti")
        cookie=cookies.SimpleCookie()
        for key in odabrani:
            int_key=int(key)
            if int_key in articles:
                cookie[str(int_key)]=articles[int_key]['price']
        print(cookie.output())

def racun():
    suma=0
    print('''<h3>Racun</h3> <br>''')
    for key in all_cookies_object:
        suma=suma+int(all_cookies_object[key].value)
    print(f"<p>Ukupan iznos: {suma}</p>")    




create_cookie()
start_html()
forma()
racun()
end_html()
