#!C:\Users\mario\AppData\Local\Programs\Python\Python313\python.exe

import cgi, os



params=cgi.FieldStorage()

ime=params.getvalue('ime')
lozinka=params.getvalue('lozinka')
lozinka2=params.getvalue('lozinka2')

print("Content-Type: text/html\n")

if lozinka != lozinka2:
    print('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Greška</title>
    </head>
    <body>
        <p style="color: red;">Lozinke se ne podudaraju! </p>
        <br>
        <a href="forma1.py">Vrati se na pocetnu formu</a>
    </body>
    </html>
    ''')


else:
  print('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <form action="forma3.py" method="post"> 
      <input type="radio" name="izbor" value="redovan"> Redovan
      <input type="radio" name="izbor" value="izvanredan"> Izvanredan <br>
      <input type="text" name="email" value="ime.prezime@gmail.com">
      Smjer:
      <select name="izbor2">
        <option value="Ekonomija"> Ekonomija </option>
        <option value="IT"> IT </option>
        <option value="Elektrotehnika"> Elektrotehnika </option>
      </select>
      <br>
      Zavrsni:
      <input type="checkbox" name="zavrsni" value="Yes">
      <input type="hidden" name="ime" value="{}">
      <input type="submit" name="objavi" value="next">
    </form>
</body>
</html>
'''.format(ime))

print(params)

print(os.environ['REQUEST_METHOD'])