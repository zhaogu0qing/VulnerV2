# -*- coding: utf-8 -*-
"""
@Time    : 2018/10/29 19:02
@Author  : zhaoguoqing600689
@File    : __init__.py.py
@Software: PyCharm
"""
from flask import Flask, redirect, url_for, render_template, request
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_mongoalchemy import MongoAlchemy

from .config import config
from . import db

bootstrap = Bootstrap()
login_manager = LoginManager()
mongodb = MongoAlchemy()

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    config_name = 'development'
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_db(app)
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
    from .forms import SearchForm
    from .vulnerability import search, get_recommend

    @app.route('/', methods=['GET', 'POST'])
    @app.route('/index', methods=['GET', 'POST'])
    def index():
        form = SearchForm()
        vulners = get_recommend()
        if request.method == 'POST':
            key = form.key.data
            key_vulners = search(key)
            return render_template('vulner/showSearch.html', vulners=key_vulners, title='Search Result')
        return render_template('index.html', vulners=vulners, form=form)
    return app







