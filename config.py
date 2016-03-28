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

number = StuInfo.query.filter_by(wechat_id='123').first()
passwd = StuInfo.query.filter_by(wechat_id='234').first()
import main.views
import wechat
