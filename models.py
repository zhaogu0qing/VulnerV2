# coding:utf8
"""
Created by zhaoguoqing on 18/11/11
"""
from flask_login import UserMixin
from bson import ObjectId
from .db import get_db

class User(UserMixin):

    def __init__(self, username=None, id=None):
        self.id = id
        self.username = username
        db = get_db()
        query = {}
        if id:
            query['_id'] = ObjectId(id)
        if username:
            query['username'] = username
        self.user = db['user'].find_one(query)
        if self.user:
            self.id = str(self.user['_id'])
            self.username = self.user['username']

    def is_exists(self):
        return self.user is not None

    def get_id(self):
        return self.id
