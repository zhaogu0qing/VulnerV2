# -*- coding: utf-8 -*-
"""
@Time    : 2018/10/29 19:02
@Author  : zhaoguoqing600689
@File    : __init__.py.py
@Software: PyCharm
"""
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from . import db

bootstrap = Bootstrap()

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('config.py', silent=True)
    app.config.from_mapping(
        MONGO_URI='mongodb://admin_zgq:ZGQ_mongodb@123.206.33.158:27017/admin',
        MONGO_DATABASE='zgq',
    )


    db.init_db(app)
    bootstrap.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import vulnerability
    app.register_blueprint(vulnerability.bp)

    @app.route('/hello')
    def hello():
        return 'Hello, world!'

    return app