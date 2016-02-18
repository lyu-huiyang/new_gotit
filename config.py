# -*- coding: utf-8 -*-
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')  # 实现CSRF保护的通用密钥,环境变量中获取
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True  # 请求结束后自动提交数据库变动
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True  # 未知, 用来消除警告 ----
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:000000@localhost:3306/new_gotit'

db = SQLAlchemy(app)
