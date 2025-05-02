#!C:/Users/mario/AppData/Local/Programs/Python/Python313/python.exe

import articles
import db
import session
import os, cgi



print("Content-Type: text/html")
session.get_or_create_session_id()
print()

params=cgi.FieldStorage()



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
    print('''<form method="POST" action="odabir.py">''')
    ispis_predmeta()
    print('''<input type="submit" value="Postavi Cookie">''')
    print('''</form>''')

def ispis_predmeta():
    for key, ime in articles.articles.items():
        print(f"<input type='checkbox' name='{key}'> {ime['name']} <br>")
  

start_html()
forma()
end_html()