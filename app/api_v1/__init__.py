# -*- coding: utf-8 -*-
"""
@Time    : 2018/10/30 19:35
@Author  : zhaoguoqing600689
@File    : __init__.py.py
@Software: PyCharm
"""
from flask import Blueprint

api = Blueprint('api', __name__)

from . import *