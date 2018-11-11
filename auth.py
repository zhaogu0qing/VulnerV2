# coding:utf8
"""
Created by zhaoguoqing on 18/11/4
"""
import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_required, login_user, logout_user
from bson import ObjectId

from .forms import RegistrationForm, LoginForm
from .db import get_db
from .models import User
from . import login_manager


bp = Blueprint('auth', __name__, url_prefix='/auth')

@login_manager.user_loader
def load_user(user_id):
    return User(id=user_id)

@bp.route('/register', methods=('GET', 'POST'))
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        db = get_db()
        db['user'].insert_one({'username': username, 'password': generate_password_hash(password)})
        flash('注册成功')
        return redirect(url_for('auth.login'))

    return render_template('auth/register.html', form=form)

@bp.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        password_hash = generate_password_hash(password)
        user = User(username=username)
        if user.is_exists() and check_password_hash(password_hash, password):
            login_user(user)
            return redirect(request.args.get('next') or url_for('index'))
        flash('无效的用户名或密码')
        return redirect(url_for('auth.login'))
    return render_template('auth/login.html', form=form)


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('你已登出')
    return redirect(url_for('index'))
