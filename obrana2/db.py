#!C:/Users/mario/AppData/Local/Programs/Python/Python313/python.exe


import json

import mysql.connector  


def get_DB_connection():
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="proba"
    )
    return mydb


def create_session():
    mydb = get_DB_connection()
    query = "INSERT INTO sesija (name) VALUES (%s)"
    values = (json.dumps({}),)
    cursor = mydb.cursor()
    cursor.execute(query, values)
    mydb.commit()
    return cursor.lastrowid 


def get_session(session_id):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM sesija WHERE session_id = %s", (session_id,))
    result = cursor.fetchone()
    if result:
        return result[0], json.loads(result[1])
    else:
        return None, {}
    


def replace_session(session_id, name):
    mydb=get_DB_connection()
    cursor=mydb.cursor()
    cursor.execute("REPLACE INTO sesija (session_id, name) VALUES (%s, %s)", (session_id,json.dumps(name)))
    mydb.commit()