# coding=utf-8
# 教务处成绩查询
import shutil
from app import app
from flask import request, render_template, flash, redirect
from ..form import JwcForm
from requests import Session
import requests
from bs4 import BeautifulSoup
from get_random_str import get_random_str
import base64
import urllib
import urllib2
import cookielib

state_dict = {
    'get_cookie': '',
    'get_view_state': ''
}


@app.route('/class', methods=['GET', 'POST'])
def zhengfang_class():
    if request.method == 'GET':
        form = JwcForm()
        login_url = 'http://210.44.176.46/'  # 正方url
        cookie_from_user = request.headers['Cookie']  # 获得用户cookie
        state_dict['get_cookie'] = cookie_from_user
        s = Session()
        s.headers['Cookie'] = cookie_from_user  # 将这个cookie保存在 爬虫s
        print 'headers cookie', s.headers['Cookie'], '\nuser cookie', state_dict['get_cookie'], '\ns.header', s.headers
        login_page = s.get(login_url)  # s先访问一下正方url并获得view_state
        soup = BeautifulSoup(login_page.content, 'html5lib')
        view_state = soup.find_all("input")
        get_view_state = view_state[0].get('value')  # 获得view_state
        state_dict['get_view_state'] = get_view_state
        print get_view_state

        response = s.get("http://210.44.176.46/CheckCode.aspx", stream=True)  # s再次刷新一下验证码url
        random_str = get_random_str()  # 获得一个随机数命名
        path = 'D:\check_code\%s.aspx' % random_str  # 保存图片的路径
        with open(path, 'wb') as f1:
            shutil.copyfileobj(response.raw, f1)  # 保存
            f1.close()
        f2 = open(r'D:\check_code\%s.aspx' % random_str, 'rb')
        ls_f = base64.b64encode(f2.read())  # 用base64模块进行读取
        f2.close()
        return render_template('class_login.html', form=form, ls_f=ls_f)


    elif request.method == 'POST':
        form = JwcForm()
        xh_post = form.number.data
        password_post = form.passwd.data
        check_code_post = form.check_code.data
        postData = {
            '__VIEWSTATE': state_dict['get_view_state'],
            'txtUserName': xh_post,
            'TextBox2': password_post,
            'txtSecretCode': check_code_post,
            'RadioButtonList1': '%D1%A7%C9%FA',
            'Button1': '',
            'lbLanguage': '',
            'hidPdrs': '',
            'hidsc': ''
        }
        default_url = 'http://210.44.176.46/default2.aspx'
        real_url = 'http://210.44.176.46/xs_main.aspx?xh=%s' % xh_post
        cookie_from_user = request.headers['Cookie']  # 获得用户cookie
        state_dict['get_cookie'] = cookie_from_user
        s = Session()
        s.headers['Cookie'] = cookie_from_user
        after_login_page = s.post(default_url,data=postData)
        soup = BeautifulSoup(after_login_page.text,"html5lib")
        print soup
        return '%s'%soup
    else:
        return u'请求非法'
