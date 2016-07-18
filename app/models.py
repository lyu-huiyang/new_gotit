# -*- coding: utf-8 -*-
from app import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    stu_number = db.Column(db.String(64), unique=True, nullable=True)
    wechat_id = db.Column(db.String(64), unique=True, nullable=True )
    zhengfang_password = db.Column(db.String(64), unique=True, nullable=True)
    library_password = db.Column(db.String(64), unique=True, nullable=True)

    def __repr__(self):
        return '<User %r>' % self.stu_number
