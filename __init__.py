# -*- coding: utf-8 -*-
"""
@Time    : 2018/10/29 19:02
@Author  : zhaoguoqing600689
@File    : __init__.py.py
@Software: PyCharm
"""
from flask import Flask, redirect, url_for, render_template
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_mongoalchemy import MongoAlchemy

from .config import config

bootstrap = Bootstrap()
login_manager = LoginManager()
mongodb = MongoAlchemy()

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    config_name = 'development'
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    mongodb.init_app(app)
    bootstrap.init_app(app)
    login_manager.session_protection = 'strong'
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import vulnerability
    app.register_blueprint(vulnerability.bp)

    from .models import Vulner

    @app.route('/')
    @app.route('/index')
    def index():
        vulners = Vulner.query.limit(5)
        return render_template('index.html', vulners=vulners)

    return app







