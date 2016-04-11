# -*- coding: utf-8 -*-
from app import app
from flask import request


@app.route('/wechat_index', methods=['GET', 'POST'])
def wechat_index():
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass
    else:
        return u"请求非法"
