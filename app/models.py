# -*- coding: utf-8 -*-
from app import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, index=True)
    stu_number = db.Column(db.String(64), unique=True, index=True)
    wechat_id = db.Column(db.String(64), unique=True, index=True)
    zhengfang_password = db.Column(db.String(64), index=True)
    library_password = db.Column(db.String(64), index=True)

    def __init__(self, stu_number, wechat_id, zhengfang_password, library_password):
        self.stu_number = stu_number
        self.wechat_id = wechat_id
        self.zhengfang_password = zhengfang_password
        self.library_password = library_password

    def __repr__(self):
        return '<User %r>' % self.stu_number


class Account(db.Model):
    """
    帐号表，用来存放id，用户名，邮箱，密码，角色值，学生学号
    """
    __tablename__ = 'accounts'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    username = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(64))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    student_number = db.Column(db.String(64), unique=True)

    def __repr__(self):
        return '<User %r>' % self.username


class Role(db.Model):
    """
    用户角色表， 用来存放id，帐号的反向引用，角色名称，权力id
    """
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    accounts = db.relationship('Account', backref='role')
    name = db.Column(db.String(64), unique=True)
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))

    def __repr__(self):
        return '<Role %r>' % self.name


class Power(db.Model):
    """
    权限表，存放id， 反向引用以及默认关闭的读、写、管理权限
    """
    __tablename__ = 'powers'
    id = db.Column(db.Integer, primary_key=True)
    roles = db.relationship('Role', backref='power')
    read_important_mess = db.Column(db.Boolean, default=False)
    update = db.Column(db.Boolean, default=False)
    admin = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<Power %r>' % self.id


class Message(db.Model):
    """
    消息表，即存放兼职信息的id， 标题， 内容
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, index=True)
    date = db.Column(db.DateTime, index=True)
    content = db.Column(db.Text, index=True)
    contact = db.Column(db.Text, index=True)

    def __repr__(self):
        return '<Message %r>' % self.title
