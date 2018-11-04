# coding:utf8
"""
Created by zhaoguoqing on 18/11/4
"""
import pymongo
from flask import current_app, g

def get_db():
    if 'db' not in g:
        g.db = pymongo.MongoClient(current_app.config['MONGO_URI'])[current_app.config['MONGO_DATABASE']]
    return g.db

def close_db():
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db(app):
    pass
    # app.teardown_appcontext(close_db)
