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

from .config import config

from . import db

bootstrap = Bootstrap()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    config_name = 'development'
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_db(app)
    bootstrap.init_app(app)
    login_manager.session_protection = 'strong'
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import vulnerability
    app.register_blueprint(vulnerability.bp)

    @app.route('/index')
    def index():
        return render_template('index.html')
        # return redirect(url_for('vulner.get_all', page_num=0))

    return app