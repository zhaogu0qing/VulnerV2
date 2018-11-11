# coding:utf8
"""
Created by zhaoguoqing on 18/11/4
"""
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '\x917\x1c\xf6\xffR\xd7\xe9c\xec\x93\x0c\x04g5>\x93\x14\xa3z\xe9;\\\x9e'
    BOOTSTRAP_SERVE_LOCAL = True
    MONGO_URI = 'mongodb://admin_zgq:ZGQ_mongodb@123.206.33.158:27017/admin'
    MONGO_DATABASE = 'zgq'
    SSL_DISABLE = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True

class ProductionConfig(Config):
    pass

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig,
}