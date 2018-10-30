# -*- coding: utf-8 -*-
"""
@Time    : 2018/10/30 19:36
@Author  : zhaoguoqing600689
@File    : manage.py.py
@Software: PyCharm
"""
from app import create_app
from flask_script import Manager

app = create_app()
manager = Manager(app)