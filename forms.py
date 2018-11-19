# coding:utf8
"""
Created by zhaoguoqing on 18/11/11
"""
from flask_wtf import FlaskForm, Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms import ValidationError

from .db import get_db
from .models import Book

class RegistrationForm(FlaskForm):

    # email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
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

    # def validate_email(self, field):
    #     db = get_db()
    #     if db['user'].find_one({'username': field.data}) is not None:
    #         raise ValidationError('该邮箱已被注册')

    def validate_username(self, field):
        db = get_db()
        if db['user'].find_one({'username': field.data}) is not None:
            raise ValidationError('该用户名已被注册')


class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(1, 64)])
    password = PasswordField('密码', validators=[DataRequired()])
    # remember_me = BooleanField('记住我')
    submit = SubmitField('登录')


class VulnerEditForm(FlaskForm):
    title = StringField('title')
    CNNVDId = StringField('CNNVDId')
    CVEId = StringField('CVEId')
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
    submit = SubmitField('提交修改')


class BookForm(Form):
    document_class = Book
    title = StringField(validators=[DataRequired()])
    author = StringField(validators=[DataRequired()])
    year = IntegerField(validators=[DataRequired()])
    submit = SubmitField('提交')
    instance = None

    def __init__(self, document=None, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        if document is not None:
            self.instance = document
            self._copy_data_to_form()

    def _copy_data_to_form(self):
        self.title.data = self.instance.title
        self.year.data = self.instance.year
        self.author.data = self.instance.author

    def save(self):
        if self.instance is None:
            self.instance = self.document_class()
        self.instance.title = self.title.data
        self.instance.year = self.year.data
        self.instance.author = self.author.data
        self.instance.save()
        return self.instance
