#!C:\Users\mario\AppData\Local\Programs\Python\Python313\python.exe

import os, cgi
from http import cookies

subjects = {
    'ip': {'name': 'Introduction to programming', 'year': 1, 'ects': 6},
    'c1': {'name': 'Calculus 1', 'year': 1, 'ects': 7},
    'cu': {'name': 'Computer usage', 'year': 1, 'ects': 5},
    'dmt': {'name': 'Digital and microprocessor technology', 'year': 1, 'ects': 6},
    'db': {'name': 'Databases', 'year': 2, 'ects': 6},
    'c2': {'name': 'Calculus 2', 'year': 2, 'ects': 7},
    'dsa': {'name': 'Data structures and algorithms', 'year': 2, 'ects': 5},
    'ca': {'name': 'Computer architecture', 'year': 2, 'ects': 6},
    'isd': {'name': 'Information systems design', 'year': 3, 'ects': 5},
    'c3': {'name': 'Calculus 3', 'year': 3, 'ects': 7},
    'sa': {'name': 'Server Architecture', 'year': 3, 'ects': 6},
    'cds': {'name': 'Computer and data security', 'year': 3, 'ects': 6}
}

year_names = {
    1: '1. godina',
    2: '2. godina',
    3: '3. godina',
    4: 'Upisni list'
}

status_names = {
    'not': 'Not selected',
    'enr': 'Enrolled',
    'pass': 'Passed'
}

def start_html():
    print("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Enrollment</title>
    </head>
    <body>
    """)

def end_html():
    print("""
    </body>
    </html>
    """)

def create_cookie():
    cookie = cookies.SimpleCookie()
    for key in params:
        cookie[key] = params.getvalue(key)
    print(cookie.output())

def checkStatus(key):
    if key in params:
        return params.getvalue(key)
    elif key in all_cookies_object:
        return all_cookies_object[key].value
    return 'Not selected'

def forma():
    print("""
    <form method="POST" action="">
    """)
    for year, label in year_names.items():
        print(f'<button type="submit" name="year" value="{year}">{label}</button>')
    print('''
    <table border="1">
        <tr>
            <td>Subjects</td>
            <td>ECTS</td>
            <td>Status</td>
        </tr>
    ''')

def forma_kraj():
    print("""
    </table>
    </form>
    """)

def predmeti(key, value):
    print(f"""
    <tr>
        <td>{value.get('name')}</td>
        <td>{value.get('ects')}</td>
        <td>
            <input type="radio" name="{key}" value="{status_names['not']}" {'checked' if checkStatus(key) == status_names['not'] else ''}>
            <label>{status_names['not']}</label>
            <input type="radio" name="{key}" value="{status_names['enr']}" {'checked' if checkStatus(key) == status_names['enr'] else ''}>
            <label>{status_names['enr']}</label>
            <input type="radio" name="{key}" value="{status_names['pass']}" {'checked' if checkStatus(key) == status_names['pass'] else ''}>
            <label>{status_names['pass']}</label>
        </td>
    </tr>
    """)

def print_list(key, value):
    print(f"""
    <tr>
        <td>{value.get('name', 'n/a')}</td>
        <td>{value.get('ects', 'n/a')}</td>
        <td>{checkStatus(key)}</td>
    </tr>
    """)

def display_subjects(year=None):
    for key, v in subjects.items():
        if year in [1, 2, 3] and v.get('year') == year:
            predmeti(key, v)
        elif year == 4:
            print_list(key, v)
         




params = cgi.FieldStorage()
cookies_string = os.environ.get('HTTP_COOKIE', '')
all_cookies_object = cookies.SimpleCookie(cookies_string)
create_cookie()
start_html()
forma()
display_subjects(int(params.getvalue('year', 1)))
forma_kraj()
end_html()
