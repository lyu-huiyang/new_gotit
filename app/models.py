# -*- coding: utf-8 -*-
from app import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    stu_number = db.Column(db.String(64), unique=True, nullable=True)
    wechat_id = db.Column(db.String(64), unique=True, nullable=True)
    zhengfang_password = db.Column(db.String(64), unique=True, nullable=True)
    library_password = db.Column(db.String(64), unique=True, nullable=True)

    def query_info(self, info):
        if info == 'id':
            return self.id
        elif info == 'stu_number':
            return self.stu_number
        elif info == 'wechat_id':
            return self.wechat_id
        else:
            pass

    def __repr__(self):
        return '<User %r>' % self.stu_number
