#!C:\Users\mario\AppData\Local\Programs\Python\Python313\python.exe

import cgi, os

params=cgi.FieldStorage()
ime=params.getvalue('ime')
email=params.getvalue('email')
izbor=params.getvalue('izbor')
izbor2=params.getvalue('izbor2')
zavrsni=params.getvalue('zavrsni')
napomena=params.getvalue('napomena')

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
    <form action="forma4.py" method="post"> 
      Ime: {}
      <br>
      E-mail: {}
      <br>
      Status: {}
      <br>
      Smjer: {}
      <br>
      Zavrsni rad: {}
      <br>
      Napomena: {}
      <br>

      <br>
      <a href="http://localhost/cgi-bin/vjezba2/forma1.py"> Vrati se na pocetak </a>
    </form>
</body>
</html>
'''.format(ime,email,izbor,izbor2,zavrsni,napomena))

print(params)

print(os.environ['REQUEST_METHOD'])