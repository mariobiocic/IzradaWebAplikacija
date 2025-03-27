#!C:\Users\mario\AppData\Local\Programs\Python\Python313\python.exe

import cgi, os

params=cgi.FieldStorage()

ime=params.getvalue('ime')

print("Content-Type: text/html\n")

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
        <option value="Baze podataka"> Ekonomija </option>
        <option value="Programiranje"> IT </option>
        <option value="Tehnicki"> Elektrotehnika </option>
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