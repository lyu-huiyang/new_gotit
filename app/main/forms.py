# -*- coding: utf-8 -*-
from flask_wtf import Form
from wtforms import SubmitField, StringField, PasswordField
from wtforms.validators import DataRequired, Length


class LibraryForm(Form):
    number = StringField(u'学号', validators=[DataRequired(), Length(1, 12)])
    passwd = PasswordField(u'密码', validators=[DataRequired()])
    submit = SubmitField(u'登陆')


class ZhengfangForm(Form):
    number = StringField(u'学号', validators=[DataRequired(), Length(1, 12)])
    passwd = PasswordField(u'密码', validators=[DataRequired()])
    check_code = StringField(u'验证码', validators=[DataRequired()])
    submit1 = SubmitField(u'登陆')


class JwcForm(Form):
    post_xuehao = StringField(u'学号', validators=[DataRequired(), Length(1, 12)])
    submit = SubmitField(u'查询')
