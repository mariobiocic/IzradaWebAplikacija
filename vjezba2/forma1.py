#!C:\Python27\python.exe

import cgi, os

params=cgi.FieldStorage()

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
    <form action="forma2.py" method="post"> 
      <input type="text" name="ime" value="">
      <input type="password" name="lozinka" value="lozinka">
      <input type="password" name="lozinka2" value="lozinka">
      <input type="submit" name="objavi" value="next">
    </form>
</body>
</html>








''')

print(params)

print(os.environ['REQUEST_METHOD'])