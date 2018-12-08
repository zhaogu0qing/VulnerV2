# -*- coding:utf-8 -*-
"""
@Time   : 2018/12/8 15:18
@Author : zhaoguoqing600689
"""
import pymongo
from flask import current_app, g

def get_db():
    if 'db' not in g:
        g.db = pymongo.MongoClient(current_app.config['MONGOALCHEMY_CONNECTION_STRING'])[current_app.config['MONGOALCHEMY_DATABASE']]
    return g.db

def close_db():
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db(app):
    pass
