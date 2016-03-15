# -*- coding: utf-8 -*-
from config import app


# 微信开发
@app.route('/wechat')
def wechat():
    return 'This is wechat page!'
