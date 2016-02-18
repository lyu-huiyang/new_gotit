# -*- coding: utf-8 -*-
from config import db



class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(64), unique=True, index=True)
    user_password = db.Column(db.String(64), unique=True, index=True)


    def __repr__(self):
        return '<User %r>' % self.user_id