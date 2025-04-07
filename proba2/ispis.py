#!C:\Users\mario\AppData\Local\Programs\Python\Python313\python.exe

import os
from http import cookies

print("Content-Type: text/html\n")  

cookies_string = os.environ.get('HTTP_COOKIE', '')
all_cookies_object = cookies.SimpleCookie(cookies_string)

print("<h3> Podaci: </h3><ul>")

if "ime" in all_cookies_object:
    print(f"<li>Ime: {all_cookies_object['ime'].value}</li>")
else:
    print("<li>Ime: Nema podataka</li>")

if "prezime" in all_cookies_object:
    print(f"<li>Prezime: {all_cookies_object['prezime'].value}</li>")
else:
    print("<li>Prezime: Nema podataka</li>")

if "mail" in all_cookies_object:
    print(f"<li>Mail: {all_cookies_object['mail'].value}</li>")
else:
    print("<li>Mail: Nema podataka</li>")

if "status" in all_cookies_object:
    print(f"<li>Status studenta: {all_cookies_object['status'].value}</li>")
else:
    print("<li>Status studenta: Nema podataka</li>")

print("</ul>")
