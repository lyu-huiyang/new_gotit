# -*- coding: utf-8 -*-
from .. import app
from ..form import LibraryForm
from flask import render_template, flash, request
from requests import Session
from pymongo import MongoClient
from ..db_operating import User, get_coll
from bs4 import BeautifulSoup

client = MongoClient("localhost", 27017)
db = client.users


@app.route('/wechat/building/library', methods=['GET', 'POST'])
def wechat_library():
    form = LibraryForm()
    number = request.args.get('xh_post')
    passwd = form.passwd.data
    if request.method == 'GET':
        return render_template('wechat_library.html', form=form, number=number)
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
            return render_template("building_finish.html", form=form)
        else:  # 登录失败返回对应提示的字符串
            flash(u'帐号或密码错误')
            return render_template('build_failed.html')
    else:
        return u'对不起，您的请求非法'


@app.route('/wechat/library_info', methods=['GET'])
def library_info():
    wechat_id = request.args.get('wechat_id')
    db = get_coll()
    info = {}
    a = db.users.find({"wechat_id": wechat_id})
    for i in a:
        info['number'] = i['stu_id']
        info['passwd'] = i['library_password']
    print '#######', info
    return render_template('no_input_library.html', number=info['number'], passwd=info['passwd'])
