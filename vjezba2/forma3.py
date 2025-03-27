#!C:\Users\mario\AppData\Local\Programs\Python\Python313\python.exe

import cgi, os

params=cgi.FieldStorage()
ime=params.getvalue('ime')
email=params.getvalue('email')
izbor=params.getvalue('izbor')
izbor2=params.getvalue('izbor2')
zavrsni=params.getvalue('zavrsni')
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
      <textarea name="napomena" placeholder="Upisi nesto"></textarea>
      <br>
      <input type="hidden" name="ime" value="{}">
      <input type="hidden" name="email" value="{}">
      <input type="hidden" name="izbor" value="{}">
      <input type="hidden" name="izbor2" value="{}">
      <input type="hidden" name="zavrsni" value="{}">
      <input type="submit" name="objavi" value="next">
    </form>
</body>
</html>








'''.format(ime,email,izbor,izbor2,zavrsni))

print(params)

print(zavrsni)

print(os.environ['REQUEST_METHOD'])