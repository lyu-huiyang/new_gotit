# -*- coding: utf-8 -*-
# 使用requests库进行抓取
import requests
from flask import Flask, request, render_template
from bs4 import BeautifulSoup
from get_random_str import get_random_str
import shutil
import base64

app = Flask(__name__)
state = {
    "view_state": "",
    "cookie": ""}


@app.route('/', methods=['GET', 'POST'])
@app.route('/class_test', methods=['GET', 'POST'])
def class_test():
    if request.method == 'GET':
        response_from_main_page = requests.get("http://210.44.176.46/")
        state['cookie'] = response_from_main_page.cookies['ASP.NET_SessionId']
        print '#############1\n\n\n\n', state['cookie']

        soup = BeautifulSoup(response_from_main_page.text, "html5lib")
        # print soup
        view_state = soup.find_all("input")
        state['view_state'] = view_state[0].get('value')
        random_str = get_random_str()
        cookies = dict({"ASP.NET_SessionId": state['cookie']})
        response_from_check_code = requests.get("http://210.44.176.46/CheckCode.aspx",
                                                cookies=cookies, stream=True)
        path = '/home/lvhuiyang/check_code/%s.aspx' % random_str

        with open(path, 'wb') as f:
            response_from_check_code.raw.decode_content = True
            shutil.copyfileobj(response_from_check_code.raw, f)

        f = open(r'/home/lvhuiyang/check_code/%s.aspx' % random_str, 'rb')
        ls_f = base64.b64encode(f.read())
        f.close()

        return render_template("test.html", ls_f=ls_f)
    elif request.method == 'POST':
        xh_post = request.form.get("number")
        password_post = request.form.get("passwd")
        check_code_post = request.form.get("check_code")
        postData = {
            '__VIEWSTATE': state['view_state'],
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

        cookies = dict({"ASP.NET_SessionId": state['cookie']})
        print '#############2\n\n\n\n', state['cookie']
        response = requests.post(default_url, data=postData, cookies=cookies)
        soup = BeautifulSoup(response.text, "html5lib")
        print soup
        return "hello"
    else:
        return 'Sorry, you are not allowed to ask this page!'


if __name__ == '__main__':
    app.run(debug=True)
