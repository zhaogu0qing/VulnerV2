# coding:utf8
"""
Created by zhaoguoqing on 18/11/11
"""
from flask_login import UserMixin
from mongoalchemy.fields import StringField, IntField, ListField

from . import mongodb as db


class Role:
    ADMIN = 0
    USER = 1

class User(db.Document, UserMixin):
    username = StringField()
    password = StringField()
    role = IntField()

    def is_exists(self):
        return self.username is not None

    def get_id(self):
        return self.mongo_id

    def is_administrator(self):
        return self.role == Role.ADMIN

class Vulner(db.Document):
    url = StringField()
    title = StringField()
    CNNVDId = StringField()
    CVEId = StringField()
    source = StringField()
    publishTime = StringField()
    updateTime = StringField()
    vulnerSource = StringField()
    vulnerLevel = StringField()
    vulnerType = StringField()
    vulnerBulletin = StringField()
    vulnerReference = StringField()
    vulnerAffect = StringField()
    threatType = StringField()
    firm = StringField()
    vulnerSummary = StringField()
    vulnerPatch = StringField()

class Site(db.Document):
    name = StringField()
    regex_list = ListField(StringField())
    host = StringField()

