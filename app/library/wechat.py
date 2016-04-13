# -*- coding: utf-8 -*-
from .. import app
from ..form import LibraryForm
from flask import render_template, flash, request
from requests import Session
from pymongo import MongoClient

client = MongoClient("localhost", 12345)
db = client.users


@app.route('/wechat/building/library', methods=['GET', 'POST'])
def wechat_library():
    form = LibraryForm()
    number = form.number.data
    passwd = form.passwd.data
    if request.method == 'GET':
        return render_template('wechat_library.html', form=form)
    elif request.method == 'POST':
        post_data = {
            "number": number,
            "passwd": passwd,
            "returnUrl": "",
            "select": "cert_no"
        }
        url_Seeeion = Session()
        temp = url_Seeeion.post("http://222.206.65.12/reader/redr_verify.php", post_data)
        book_list_url = url_Seeeion.get("http://222.206.65.12/reader/book_lst.php")
        if book_list_url.url == 'http://222.206.65.12/reader/book_lst.php':  # url相同意味着登陆成功
            db.users.update({"stu_id": number}, {"$set": {"library_password": passwd}})
            return render_template("building_finish.html")
        else:  # 登录失败返回对应提示的字符串
            flash(u'帐号或密码错误')
            return render_template('library_login.html', form=form)
    else:
        return u'对不起，您的请求非法'
