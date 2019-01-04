# -*- coding:utf-8 -*-
"""
@Time   : 2018/12/8 15:18
@Author : zhaoguoqing600689
"""
from math import ceil

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


class Pagination(object):

    def __init__(self, total, page=None, page_limit=10):
        self.total = total
        self.page = page
        self.page_limit = page_limit
        self.items = []

    @property
    def pages(self):
        """The total number of pages"""
        return int(ceil(self.total / float(self.page_limit)))

    def has_prev(self):
        return self.page > 1

    @property
    def prev_num(self):
        """The previous page number."""
        return self.page - 1

    @property
    def next_num(self):
        """The next page number."""
        return self.page + 1

    def has_next(self):
        """Returns ``True`` if a next page exists."""
        return self.page < self.pages
