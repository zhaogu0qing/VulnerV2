# coding:utf8
"""
Created by zhaoguoqing on 18/11/4
"""
import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from .db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif db['user'].find_one({'username': username}) is not None:
            error = 'User {} is already registered.'.format(username)

        if error is None:
            db['user'].insert_one({'username': username, 'password': generate_password_hash(password)})
            return redirect(url_for('auth.login'))

        flash(error)

    return render_template('auth/register.html')
