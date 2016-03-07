# -*- coding: utf-8 -*-
from flask_wtf import Form
from wtforms import SubmitField, DateField, StringField, PasswordField, SelectField
from wtforms.validators import DataRequired, Length


class LibraryForm(Form):
    number = StringField(u'学号', validators=[DataRequired(), Length(1, 12)])
    passwd = PasswordField(u'密码', validators=[DataRequired()])
    submit1 = SubmitField(u'登陆')


class EcardForm(Form):
    number = StringField(u'学号', validators=[DataRequired(), Length(1, 12)])
    submit = SubmitField('Submit')


class JwcForm(Form):
    number = StringField(u'学号', validators=[DataRequired(), Length(1, 12)])
    passwd = PasswordField(u'密码', validators=[DataRequired()])
    check_code = StringField(u'验证码', validators=[DataRequired()])
    submit1 = SubmitField(u'登陆')

class ScoreForm(Form):
    post_xuehao = StringField(u'学号', validators=[DataRequired(), Length(1, 12)])
    submit = SubmitField('Submit')
