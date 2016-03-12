# -*- coding: utf-8 -*-
from flask_wtf import Form
from wtforms import SubmitField, StringField, PasswordField, SelectField, FieldList
from wtforms.validators import DataRequired, Length


class LibraryForm(Form):
    number = StringField(u'学号', validators=[DataRequired(), Length(1, 12)])
    passwd = PasswordField(u'密码', validators=[DataRequired()])
    submit = SubmitField(u'登陆')

class LibraryHistForm(Form):
    number = StringField(u'学号', validators=[DataRequired(), Length(1, 12)])
    passwd = PasswordField(u'密码', validators=[DataRequired()])
    submit = SubmitField(u'登陆')



class JwcForm(Form):
    number = StringField(u'学号', validators=[DataRequired(), Length(1, 12)])
    passwd = PasswordField(u'密码', validators=[DataRequired()])
    check_code = StringField(u'验证码', validators=[DataRequired()])
    submit1 = SubmitField(u'登陆')


class ScoreForm(Form):
    post_xuehao = StringField(u'学号', validators=[DataRequired(), Length(1, 12)])
    submit = SubmitField(u'查询')


class CetForm(Form):
    name = StringField(u'姓名', validators=[DataRequired(), Length(1, 12)])
    number = StringField(u'准考证号', validators=[DataRequired(), Length(1, 16)])
    submit = SubmitField(u'查询')


