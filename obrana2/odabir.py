#!C:/Users/mario/AppData/Local/Programs/Python/Python313/python.exe


import cgi

import session


print("Content-Type: text/html")
print()

params=cgi.FieldStorage()

session.insert_session_data(params)

session_data=session.get_session_data()


print("""
    <!DOCTYPE HTML>
      <html>
      <head><title>Odabir</title></head>
      <body>
      <h2>Odabrani Artikli</h2>
      """)

if session_data:
    for article_id, article_info in session_data.items():
        if article_id.isdigit():
            name = article_info.get("name")
            print(f"{name}")
else:
    print("nije nis odabrano")

print("""
      <br>
      <a href="index.py">Povratak </a>
</body>
      </html>
      """)