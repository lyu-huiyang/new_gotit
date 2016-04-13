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


@app.route('wechat/library_info', methods=['GET', 'POST'])
def library_info():
    wechat_id = request.args.grt('wechat_id')
    db = get_coll()
    a = db.users.find({"wechat_id": wechat_id}, {"wechat_id": 1, "_id": 0})
    for i in a:
        number = i['stu_id']
        passwd = i['library_password']
    login_url = 'http://222.206.65.12/reader/redr_verify.php'
    book_hist_url = 'http://222.206.65.12/reader/book_hist.php'
    data = {
        'number': number,
        'passwd': passwd,
        'returnUrl': '',
        'select': 'cert_no'
    }
    url_session = Session()

    temp = url_session.post(login_url, data=data)
    hist_data = {
        'para_string': 'all'
    }
    book_hist = url_session.post(book_hist_url, data=hist_data)
    page_content = book_hist.content
    soup = BeautifulSoup(page_content, 'html5lib')
    html_td = soup.find_all('td', bgcolor="#FFFFFF")
    print 'len --> html_td', len(html_td)
    j = 0
    books = []
    abook = {}
    # print html_td[13].get_text().strip()
    for i in range(0, len(html_td) / 7):
        abook['xuhao'] = html_td[j].get_text().strip()
        abook['number'] = html_td[j + 1].get_text().strip()
        abook['name'] = html_td[j + 2].get_text().strip()
        abook['author'] = html_td[j + 3].get_text().strip()
        abook['borrowing_date'] = html_td[j + 4].get_text().strip()
        abook['return_date'] = html_td[j + 5].get_text().strip()
        abook['position'] = html_td[j + 6].get_text().strip()

        j += 7
        books.append(abook)
        abook = {}

    return render_template('book_history.html', books=books)
