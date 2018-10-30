# -*- coding: utf-8 -*-
"""
@Time    : 2018/10/30 19:34
@Author  : zhaoguoqing600689
@File    : __init__.py.py
@Software: PyCharm
"""
from flask import Flask
from ..config import *


def create_app():
    app = Flask(__name__)
    # app.config.from_object()

    from .api_v1 import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api/v1')