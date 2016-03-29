# -*- coding: utf-8 -*-
"""
The flask application package.
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "hard to guess string"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:000000@localhost/gotit'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)


class StuInfo(db.Model):
    __tablename__ = 'stu_info'
    id = db.Column(db.Integer, primary_key=True)
    stu_id = db.Column(db.String(64), unique=True)
    wechat_id = db.Column(db.String(64), unique=True)
    jwc_password = db.Column(db.String(64), unique=True)
    library_password = db.Column(db.String(64), unique=True)

    def __repr__(self):
        return '<Role %r>' % self.stu_id


class StuClass(db.Model):
    __tablename__ = 'stu_class'
    id = db.Column(db.Integer, primary_key=True)
    stu_id = db.Column(db.String(64), unique=True)
    wechat_id = db.Column(db.String(64), unique=True)
    monday_12 = db.Column(db.String(128), unique=True)
    monday_34 = db.Column(db.String(128), unique=True)
    monday_56 = db.Column(db.String(128), unique=True)
    monday_78 = db.Column(db.String(128), unique=True)
    monday_910 = db.Column(db.String(128), unique=True)
    tuesday_12 = db.Column(db.String(128), unique=True)
    tuesday_34 = db.Column(db.String(128), unique=True)
    tuesday_56 = db.Column(db.String(128), unique=True)
    tuesday_78 = db.Column(db.String(128), unique=True)
    tuesday_910 = db.Column(db.String(128), unique=True)
    wednesday_12 = db.Column(db.String(128), unique=True)
    wednesday_34 = db.Column(db.String(128), unique=True)
    wednesday_56 = db.Column(db.String(128), unique=True)
    wednesday_78 = db.Column(db.String(128), unique=True)
    wednesday_90 = db.Column(db.String(128), unique=True)
    thursday_12 = db.Column(db.String(128), unique=True)
    thursday_34 = db.Column(db.String(128), unique=True)
    thursday_56 = db.Column(db.String(128), unique=True)
    thursday_78 = db.Column(db.String(128), unique=True)
    thursday_910 = db.Column(db.String(128), unique=True)
    friday_12 = db.Column(db.String(128), unique=True)
    friday_34 = db.Column(db.String(128), unique=True)
    friday_56 = db.Column(db.String(128), unique=True)
    friday_78 = db.Column(db.String(128), unique=True)
    friday_910 = db.Column(db.String(128), unique=True)
    saturday_12 = db.Column(db.String(128), unique=True)
    saturday_34 = db.Column(db.String(128), unique=True)
    saturday_56 = db.Column(db.String(128), unique=True)
    saturday_78 = db.Column(db.String(128), unique=True)
    saturday_910 = db.Column(db.String(128), unique=True)
    sunday_12 = db.Column(db.String(128), unique=True)
    sunday_34 = db.Column(db.String(128), unique=True)
    sunday_56 = db.Column(db.String(128), unique=True)
    sunday_78 = db.Column(db.String(128), unique=True)
    sunday_910 = db.Column(db.String(128), unique=True)

    def __repr__(self):
        return '<Role %r>' % self.stu_id


import main.views
import wechat
