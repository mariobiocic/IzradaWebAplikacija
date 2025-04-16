#!C:\Users\mario\AppData\Local\Programs\Python\Python313\python.exe



import os, cgi
from http import cookies

print("Content-Type: text/html\n")

articles ={ 1 : {"name":"CPU", "price" : 400 },
            2 : {"name":"RAM", "price" : 200},
            3 : {"name":"GPU", "price" : 300},
            4 : {"name":"HDD", "price" : 250},
            5 : {"name":"DVD", "price" : 4150}
            }

cookies_string = os.environ.get('HTTP_COOKIE', '')
all_cookies_object = cookies.SimpleCookie(cookies_string)

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

def suma():
    total_price = 0
    for key, morsel in all_cookies_object.items():
        try:
            naziv, cijena = morsel.value.split(":")
            cijena = int(cijena)
            total_price += cijena
        except ValueError:
            print(f"<p>Greška u formatu podatka za stavku: {morsel.value}</p>")
    
    print(f"<p>Cijena u kosarici: {total_price}</p>")

def imena_odabranih():
    print('''<h3>Postojeci cookie</h3><ul>''') 
    for key, data in all_cookies_object.items():
        naziv, cijena = data.value.split(":")  
        print(f"<li>{naziv} - Cijena: {cijena} kn</li>")
    print('''</ul>''')   

start_html()
suma() 
imena_odabranih()
end_html()
