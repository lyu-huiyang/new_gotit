# -*- coding: utf-8 -*-
from .. import app
from ..form import LibraryForm
from flask import render_template, request
from requests import Session
from bs4 import BeautifulSoup
import json


@app.route('/library2', methods=['GET', 'POST'])
def library2():
    form = LibraryForm()
    number = form.number.data
    passwd = form.passwd.data
    if request.method == 'GET':
        return u'对不起，您的请求非法'
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
            soup = BeautifulSoup(book_list_url.text, 'html5lib')
            html_td = soup.find_all('td', bgcolor="#FFFFFF")
            try:
                j = 0
                books = []
                abook = {}
                # print html_td[5].get_text().strip()
                for i in range(0, len(html_td) / 8):
                    abook['number'] = html_td[j].get_text().strip()
                    abook['name'] = html_td[j + 1].get_text().strip()
                    abook['author'] = html_td[j + 2].get_text().strip()
                    abook['borrowing_date'] = html_td[j + 3].get_text().strip()
                    abook['return_date'] = html_td[j + 4].get_text().strip()
                    abook['continue'] = u'续借'
                    j += 8
                    books.append(abook)
                    abook = {}
                return json.dumps(books)
            except:
                return "No books"
        else:  # 登录失败返回对应提示的字符串
            return "number or password is wrong"
    else:
        return u'对不起，您的请求非法'
