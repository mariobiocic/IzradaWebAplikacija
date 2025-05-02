#!C:/Users/mario/AppData/Local/Programs/Python/Python313/python.exe


import db

import os

from http import cookies

import articles



def get_or_create_session_id():
    cookie_str = os.environ.get('HTTP_COOKIE', '')
    cookie = cookies.SimpleCookie(cookie_str)
    session_id = cookie.get("session_id").value if cookie.get("session_id") else None
    if session_id is None:
        session_id = db.create_session()
        cookies_object = cookies.SimpleCookie()
        cookies_object["session_id"] = session_id
        print(cookies_object.output()) 
    return session_id



def get_session_data():
    session_id = get_or_create_session_id()
    _, name = db.get_session(session_id)
    return name




def insert_session_data(params):
    session_id=get_or_create_session_id()
    _,name=db.get_session(session_id)
    for article_id in params.keys():
        art_id = int(article_id)
        art = articles.articles.get(art_id)
        if art:
            name[article_id] = art

    db.replace_session(session_id, name)