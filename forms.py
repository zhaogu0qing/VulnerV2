# coding:utf8
"""
Created by zhaoguoqing on 18/11/11
"""
from flask_wtf import FlaskForm, Form
from werkzeug.security import check_password_hash
from wtforms import StringField, PasswordField, BooleanField, SubmitField, \
    TextAreaField, IntegerField, SelectField, RadioField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms import ValidationError

from .models import User

class RegistrationForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired(),
                                                   Length(1, 64),
                                                   Regexp('^([\u4e00-\u9fa5]|[A-Za-z0-9_.])*$',
                                                          0,
                                                          '用户名只能包含中文/字母/数字/./下划线',
                                                          )])
    password = PasswordField('密码', validators=[DataRequired()
        ,
        EqualTo('password2', message='两次密码必须一致!'),
    ])

    password2 = PasswordField('确认密码', validators=[DataRequired()
        ,
    ])



    submit = SubmitField('注册')

    def validate_username(self, field):
        if User.query.filter(User.username == field.data).first() is not None:
            raise ValidationError('该用户名已被注册')

class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(1, 64)])
    password = PasswordField('密码', validators=[DataRequired()])
    # remember_me = BooleanField('记住我')
    submit = SubmitField('登录')

class VulnerEditForm(FlaskForm):
    title = TextAreaField('title')
    CNNVDId = StringField('CNNVDId')
    CVEId = StringField('CVEId')
    source = StringField('source')
    publishTime = StringField('publishTime')
    updateTime = StringField('updateTime')
    vulnerSource = TextAreaField('vulnerSource')
    vulnerLevel = StringField('vulnerLevel')
    vulnerType = StringField('vulnerType')
    threatType = StringField('threatType')
    firm = StringField('firm')
    vulnerSummary = TextAreaField('vulnerSummary')
    vulnerBulletin = TextAreaField('vulnerBulletin')
    vulnerReference = TextAreaField('vulnerReference')
    vulnerAffect = TextAreaField('vulnerAffect')
    vulnerPatch = TextAreaField('vulnerPatch')
    tag = StringField('tag')
    submit = SubmitField('提交修改')

class UserForm(FlaskForm):
    document_class = User
    username = StringField('用户名', validators=[DataRequired()])
    role = SelectField('角色', coerce=int, choices=[(0, 'admin'), (1, 'user')], validators=[DataRequired()])
    submit = SubmitField('提交')

class ChangePasswordForm(FlaskForm):
    old_password = StringField('旧密码', validators=[DataRequired()])
    new_password = StringField('新密码', validators=[DataRequired()])
    submit = SubmitField('提交')

class SearchForm(FlaskForm):
    key = StringField(validators=[DataRequired()])
    submit = SubmitField('搜索')


