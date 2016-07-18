# -*- coding: utf-8 -*-
from .. import wechat
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
from ..forms import ZhengfangForm
from ..forms import LibraryForm
from bs4 import BeautifulSoup
from ...get_random_str import get_random_str
from requests import Session
from app import db
from app.models import User
import requests
import shutil
import base64
import redis

pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=0)
r = redis.Redis(connection_pool=pool)


def save(stu_number, wechat_id, zhengfang_password, library_password):
    stu_info = User(
        stu_number=stu_number,
        wechat_id=wechat_id,
        zhengfang_password=zhengfang_password,
        library_password=library_password
    )
    db.session.add(stu_info)
    db.session.commit()


@wechat.route('/building/zhengfang', methods=['GET', 'POST'])
def zhengfang_building():
    if request.method == 'GET':
        wechat_id = request.args.get('wechat_id')
        if wechat_id is None:
            return u'请求非法'
        form = ZhengfangForm()
        headers1 = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Host': '210.44.176.46',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36'
        }
        # 登陆首页
        response_from_main_page = requests.get("http://210.44.176.46/", headers=headers1)
        cookies = response_from_main_page.cookies['ASP.NET_SessionId']
        soup = BeautifulSoup(response_from_main_page.text, "html5lib")
        view_state = soup.find_all("input")
        view_state = view_state[0].get('value')
        random_str = get_random_str()

        headers2 = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': 'ASP.NET_SessionId=%s' % cookies,
            'Host': '210.44.176.46',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36'
        }

        cookies = dict({"ASP.NET_SessionId": cookies})
        response_from_check_code = requests.get(
            "http://210.44.176.46/CheckCode.aspx",
            headers=headers2,
            cookies=cookies,
            stream=True
        )
        path = '/home/lvhuiyang/check_code/%s.aspx' % random_str
        with open(path, 'wb') as f:
            response_from_check_code.raw.decode_content = True
            shutil.copyfileobj(response_from_check_code.raw, f)

        f = open(r'/home/lvhuiyang/check_code/%s.aspx' % random_str, 'rb')
        ls_f = base64.b64encode(f.read())
        f.close()
        r.set(ls_f, cookies["ASP.NET_SessionId"])
        r.set(cookies["ASP.NET_SessionId"], view_state)
        return render_template('wechat/zhengfang_building.html', form=form, ls_f=ls_f, wechat_id=wechat_id)


    elif request.method == 'POST':
        form = ZhengfangForm()
        xh_post = form.number.data
        password_post = form.passwd.data
        check_code_post = form.check_code.data
        wechat_id = request.form.get("wechat_id")
        check_base64 = request.form.get("check_base64")
        cookies = r.get(check_base64)
        view_state = r.get(cookies)
        cookies = dict({"ASP.NET_SessionId": cookies})

        post_data = {
            '__VIEWSTATE': view_state,
            'TextBox1': xh_post,
            'TextBox2': password_post,
            'TextBox3': check_code_post,
            'RadioButtonList1': '%D1%A7%C9%FA',
            'Button1': '',
            'hidPdrs': '',
            'hidsc': ''
        }
        headers3 = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Content-Length': '292',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': 'ASP.NET_SessionId=%s' % cookies['ASP.NET_SessionId'],
            'Host': '210.44.176.46',
            'Origin': 'http://210.44.176.46',
            'Referer': 'http://210.44.176.46/',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36'
        }

        default_url = 'http://210.44.176.46/default5.aspx'
        real_url = 'http://210.44.176.46/xs_main.aspx?xh=%s' % xh_post

        # 登陆到用户首页
        response = requests.post(default_url, data=post_data, headers=headers3, cookies=cookies)

        try:
            headers4 = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Encoding': 'gzip, deflate, sdch',
                'Accept-Language': 'zh-CN,zh;q=0.8',
                'Connection': 'keep-alive',
                'Host': '210.44.176.46',
                'Referer': real_url,
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36'
            }

            class_page = 'http://210.44.176.46/xskbcx.aspx?xh=%s&xm=%s&gnmkdm=N121603' % (xh_post, password_post)
            postData2 = {
                'xh': xh_post,
                'xm': '',
                'gnmkdm': 'N121603'
            }
            score_response = requests.get(class_page, headers=headers4, cookies=cookies, data=postData2)
            soup = BeautifulSoup(score_response.text, "html5lib")
            stu_info = []
            stu_id = soup.find_all("span")[3].get_text().strip()
            stu_name = soup.find_all("span")[4].get_text().strip()
            stu_school = soup.find_all("span")[5].get_text().strip()
            stu_zhuanye = soup.find_all("span")[6].get_text().strip()
            stu_class = soup.find_all("span")[7].get_text().strip()

            stu_info.append(stu_id)
            stu_info.append(stu_name)
            stu_info.append(stu_school)
            stu_info.append(stu_zhuanye)
            stu_info.append(stu_class)

            all_classes = []
            class_12_list = []
            class_34_list = []
            class_56_list = []
            class_78_list = []
            class_9_list = []

            classes = soup.find_all("tr")

            for i1 in classes[4].find_all("td", width="7%"):
                class_12_list.append(i1.get_text().strip())

            for i2 in classes[6].find_all("td", align="Center"):
                class_34_list.append(i2.get_text().strip())

            for i in classes[8].find_all("td", align="Center"):
                class_56_list.append(i.get_text().strip())

            for i in classes[10].find_all("td", align="Center"):
                class_78_list.append(i.get_text().strip())

            for i in classes[12].find_all("td", align="Center"):
                class_9_list.append(i.get_text().strip())

            all_classes.append(class_12_list)
            all_classes.append(class_34_list)
            all_classes.append(class_56_list)
            all_classes.append(class_78_list)
            all_classes.append(class_9_list)

            return_info = []
            return_info.append(stu_info)
            return_info.append(all_classes)

            return redirect(
                url_for('wechat.library_building', number=xh_post, zhengfang_token=password_post, wechat_id=wechat_id))
            # return render_template('wechat/library_building.html', number=xh_post, form=LibraryForm())
        except:
            return render_template("wechat/error.html", message=u'您输入的密码或验证码有问题，请您关闭页面重新进行绑定')
    else:
        return 'Sorry, you are not allowed to ask this page!'


@wechat.route('/building/library', methods=['GET', 'POST'])
def library_building():
    form = LibraryForm()
    number = request.args.get('number')
    wechat_id = request.args.get('wechat_id')
    zhengfang_password = request.args.get('zhengfang_token')
    library_passwd = form.passwd.data
    if request.method == 'GET':
        return render_template('wechat/library_building.html', form=form, number=number)
    elif request.method == 'POST':
        post_data = {
            "number": number,
            "passwd": library_passwd,
            "returnUrl": "",
            "select": "cert_no"
        }
        url_Seeeion = Session()
        temp = url_Seeeion.post("http://222.206.65.12/reader/redr_verify.php", post_data)
        book_list_url = url_Seeeion.get("http://222.206.65.12/reader/book_lst.php")
        if book_list_url.url == 'http://222.206.65.12/reader/book_lst.php':  # url相同意味着登陆成功
            save(
                stu_number=number,
                wechat_id=wechat_id,
                zhengfang_password=zhengfang_password,
                library_password=library_passwd
            )
            return render_template("wechat/error.html", message=u'绑定成功，感谢您的使用，现在您可以关闭此页面了')
        else:  # 登录失败返回对应提示的字符串
            return render_template("wechat/error.html", message=u'您输入的密码错误，请您关闭页面重新进行绑定')
    else:
        return u'对不起，您的请求非法'
