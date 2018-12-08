# coding:utf8
"""
Created by zhaoguoqing on 18/11/4
"""
import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for,
    jsonify, abort)
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_required, login_user, logout_user, current_user
from bson import ObjectId, json_util

from .forms import *
from .models import User
from .decorators import admin_required
from . import login_manager

bp = Blueprint('auth', __name__, url_prefix='/auth')

@login_manager.user_loader
def load_user(user_id):
    return User.query.get_or_404(mongo_id=user_id)

@bp.route('/register', methods=('GET', 'POST'))
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User(username=username, password=generate_password_hash(password), role='user')
        user.save()
        flash('注册成功')
        return redirect(url_for('auth.login'))

    return render_template('auth/register.html', form=form)

@bp.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.query.filter(User.username == username).first()
        if user and check_password_hash(user.password, password):
            user.mongo_id = str(user.mongo_id)
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


@bp.route('/list_user')
@bp.route('/list_user/<int:page>')
@login_required
@admin_required
def list_user(page=1):
    pagination = User.query.paginate(page=page, per_page=5)
    return render_template('auth/list_user.html', title='所有用户', pagination=pagination)

@bp.route('/delete/<user_id>')
@login_required
@admin_required
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    user.remove()
    return redirect(url_for('auth.list_user'))

@bp.route('/edit_user/<user_id>', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_user(user_id):
    user = User.query.get_or_404(user_id)
    form = UserForm(username=user.username, role=user.role)
    if request.method == 'GET':
        return render_template('auth/UserFormEdit.html', form=form, title='edit user')
    else:
        user.username = form.username.data
        user.role = form.role.data
        user.save()
        return redirect(url_for('auth.list_user'))



@bp.route('/change_password', methods=['GET', 'POST'])
def change_password():
    form = ChangePasswordForm()
    if form.validate_on_submit():
        if check_password_hash(current_user.password, form.old_password.data):
            current_user.password = generate_password_hash(form.new_password.data)
            current_user.save()
        else:
            flash("旧密码错误")
            return redirect(url_for('auth.change_password'))
        return redirect(url_for('index'))
    return render_template('baseFormEdit.html', form=form, title='修改密码')





