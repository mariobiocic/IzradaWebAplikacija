#!C:/Users/mario/AppData/Local/Programs/Python/Python313/python.exe
import os
from http import cookies
import mysql.connector  # Corrected import statement

print("Content-Type: text/html; charset=UTF-8\n")

# Retrieve cookies from the request
cookies_string = os.environ.get('HTTP_COOKIE', '')
all_cookies = cookies.SimpleCookie(cookies_string)

if "session_id" in all_cookies:
    session_id = all_cookies["session_id"].value

    try:
        # Correct database connection
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="odabir_predmeta"  # Fixed missing closing quote
        )

        cursor = db.cursor()
        cursor.execute("DELETE FROM sesije WHERE session_id=%s", (session_id,))
        db.commit()
        cursor.close()
        db.close()

        # Clear the session cookie
        print(f"Set-Cookie: session_id=; expires=Thu, 26 April 2025 00:00:00 GMT; path=/")
        print("<p>Uspjesno ste se odjavili. <a href='login.py'>Prijavite se ponovno</a></p>")
    except mysql.connector.Error as err:
        # Error handling for database connection or query execution
        print(f"<p>Greška pri radu s bazom podataka: {err}</p>")
else:
    print("<p>Nemate aktivnu sesiju.</p>")