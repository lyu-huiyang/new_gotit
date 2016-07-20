# coding=utf-8
from flask import render_template
from flask import flash
from flask import request
from requests import Session
from app.models import User
from bs4 import BeautifulSoup
from ..forms import LibraryForm
from .. import wechat


# 图书借阅页面
@wechat.route('/library', methods=['GET', 'POST'])
def library():
    form = LibraryForm()
    if request.method == 'GET':
        wechat_id = request.args.get('wechat_id')
        account = User.query.filter_by(wechat_id=wechat_id).first()
        return render_template(
            'wechat/library_login.html',
            form=form,
            number=account.stu_number,
            passwd=account.library_password,
            wechat_id=wechat_id
        )
    elif request.method == 'POST':
        number = form.number.data
        passwd = form.passwd.data
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
                return render_template('main/library.html', books=books, number=number, passwd=passwd)
            except:
                return render_template('main/library_no_books.html', number=number, passwd=passwd)
        else:  # 登录失败返回对应提示的字符串
            flash(u'帐号或密码错误')
            return render_template('main/library_login.html', form=form)
    else:
        return u'对不起，您的请求非法'
