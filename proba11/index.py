#!C:\Users\mario\AppData\Local\Programs\Python\Python313\python.exe

import os, cgi
from http import cookies

params=cgi.FieldStorage()
cookies_string=os.environ.get('HTTP_COOKIE','')
all_cookies_object=cookies.SimpleCookie(cookies_string)


translations = {
    'hr' : {'index':'Kuca', 'articles':'Proizvodi','contact':'Kontakt','basket':'Kosarica'},
    'eng' : {'index':'Home', 'articles':'Articles','contact':'Contact','basket':'Basket'},
    'de' : {'index':'Haus', 'articles':'Artikeln','contact':'Kontakt','basket':'Verkaufstasche'}
}

def create_cookie():
    if "lang" in params:
        odabrani=params.getvalue("lang")
        cookie=cookies.SimpleCookie()
        cookie["lang"]=odabrani
        print(cookie.output())

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
    <div>''')
    print(f'''<a href="index.py"> {translations[current_lang]['index']} </a>''')
    print(f'''<a href="articles.py"> {translations[current_lang]['articles']} </a>''')
    print(f'''<a href="basket.py"> {translations[current_lang]['basket']} </a>''')
    print(f'''<a href="contact.py"> {translations[current_lang]['contact']} </a>''')
    print('''</div>
    
    ''')

def forma():
    print('''<form method="post" action="">''')
    print(f"""<input type='radio' name='lang' value='hr' {'checked' if current_lang == 'hr' else ''}> Hrvatski <br>""")
    print(f"""<input type='radio' name='lang' value='eng' {'checked' if current_lang == 'eng' else ''}> Engleski <br>""")
    print(f"""<input type='radio' name='lang' value='de' {'checked' if current_lang == 'de' else ''}> Njemacki <br>""")
    print('''<input type="submit" value="Odaberi jezik">''')
    print('''</form>''')

def end_html():
    print('''
    </body>
    </html>
    ''')

create_cookie()

if "lang" in params:
    current_lang=params.getvalue("lang")
elif "lang" in all_cookies_object:
    current_lang=all_cookies_object["lang"].value
else:
    current_lang="hr"


start_html()
forma()
end_html()