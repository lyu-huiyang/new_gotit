# -*- coding: utf-8 -*-
from ...get_random_str import get_random_str
from ..forms import ZhengfangForm
from bs4 import BeautifulSoup
from flask import request
from flask import render_template
from flask import flash
from flask import redirect
from .. import wechat
from app.models import User
import requests
import shutil
import base64
import redis

pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=0)
r = redis.Redis(connection_pool=pool)


@wechat.route('/zhengfang', methods=['GET', 'POST'])
def zhengfang():
    wechat_id = request.args.get('wechat_id')
    account = User.query.filter_by(wechat_id=wechat_id).first()
    if request.method == 'GET':
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
        return render_template(
            'wechat/zhengfang_login.html',
            form=form, ls_f=ls_f,
            number=account.stu_number,
            passwd=account.zhengfang_password
        )


    elif request.method == 'POST':
        form = ZhengfangForm()
        xh_post = form.number.data
        password_post = form.passwd.data
        check_code_post = form.check_code.data
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
                'Cookie': cookies["ASP.NET_SessionId"],
                'Host': '210.44.176.46',
                'Referer': real_url,
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36'
            }
            password_post = ''
            score_page = "http://210.44.176.46/xscjcx.aspx?xh=%s&xm=%r&gnmkdm=N121605" % (xh_post, password_post)
            score_response = requests.get(score_page, headers=headers4, cookies=cookies)
            soup = BeautifulSoup(score_response.text, "html5lib")

            soup_input = soup.find_all("input")
            score_view_state = soup_input[2].get('value')
            html_span = soup.find_all("span")

            stu_base_info = {}
            stu_base_info['stu_id'] = html_span[5].get_text().strip()
            stu_base_info['stu_name'] = html_span[6].get_text().strip()
            stu_base_info['stu_school'] = html_span[7].get_text().strip()
            stu_base_info['stu_major'] = html_span[8].get_text().strip() + html_span[9].get_text().strip()
            stu_base_info['stu_major_direction'] = html_span[10].get_text().strip()
            stu_base_info['stu_class'] = html_span[11].get_text().strip()

            html_td = soup.find_all("td")
            class_info = []
            not_pass_class = {}
            not_pass_class_len = (len(html_td) - 27) / 6
            for i in range(0, not_pass_class_len):
                not_pass_class['number'] = html_td[i * 6 + 14].get_text().strip()
                not_pass_class['class_name'] = html_td[i * 6 + 15].get_text().strip()
                not_pass_class['class_property'] = html_td[i * 6 + 16].get_text().strip()
                not_pass_class['grade_point'] = html_td[i * 6 + 17].get_text().strip()
                not_pass_class['max_point'] = html_td[i * 6 + 18].get_text().strip()
                not_pass_class['class_return'] = html_td[i * 6 + 19].get_text().strip()
                class_info.append(not_pass_class)
                not_pass_class = {}

            # 获取该学生的年级 eg.14  15
            stu_id = stu_base_info['stu_id'][-11:-9]

            def post_for_score(ddlXN, ddlXQ):
                headers2 = {
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                    'Accept-Encoding': 'gzip, deflate, sdch',
                    'Accept-Language': 'zh-CN,zh;q=0.8',
                    'Connection': 'keep-alive',
                    'Host': '210.44.176.46',
                    'Referer': score_page,
                    'Upgrade-Insecure-Requests': '1',
                    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36'
                }
                # headers2['Referer'] = score_page
                postData2 = {
                    '__EVENTTARGET': '',
                    '__EVENTARGUMENT': '',
                    '__VIEWSTATE': score_view_state,
                    'hidLanguage': '',
                    'ddlXN': ddlXN,
                    'ddlXQ': ddlXQ,
                    'ddl_kcxz': '',
                    'btn_xq': ''
                }
                request3 = requests.post(score_page, data=postData2, headers=headers2, cookies=cookies)
                soup = BeautifulSoup(request3.text, 'html.parser', from_encoding="utf-8")

                data_list = soup.find_all("td")
                length = (len(data_list) - 36) / 15
                count = 23
                temp = {}
                return_data = []
                for i in range(0, length):
                    temp['year'] = data_list[count].get_text().strip()  # 学年
                    temp['term'] = data_list[count + 1].get_text().strip()  # 学期
                    temp['class_code'] = data_list[count + 2].get_text().strip()  # 课程代码
                    temp['class_name'] = data_list[count + 3].get_text().strip()  # 课程名称
                    temp['class_quality'] = data_list[count + 4].get_text().strip()  # 课程性质
                    temp['class_return'] = data_list[count + 5].get_text().strip()  # 课程归属
                    temp['score_point'] = data_list[count + 6].get_text().strip()  # 学分
                    temp['gpa'] = data_list[count + 7].get_text().strip()  # 绩点
                    temp['point'] = data_list[count + 8].get_text().strip()  # 成绩
                    temp['flag'] = data_list[count + 9].get_text().strip()  # 标记
                    temp['second_point'] = data_list[count + 10].get_text().strip()  # 补考成绩
                    temp['third_point'] = data_list[count + 11].get_text().strip()  # 重修成绩
                    temp['school'] = data_list[count + 12].get_text().strip()  # 学院
                    temp['comment'] = data_list[count + 13].get_text().strip()  # 备注
                    temp['second_flag'] = data_list[count + 14].get_text().strip()  # 重修标记
                    return_data.append(temp)
                    temp = {}
                    count += 15
                return return_data

            if stu_id == "13":
                score_content = [post_for_score("2015-2016", "1"),
                                 post_for_score("2014-2015", "1"), post_for_score("2014-2015", "2"),
                                 post_for_score("2013-2014", "1"), post_for_score("2013-2014", "2"),
                                 post_for_score("2015-2016", "2")]

            elif stu_id == "14":
                score_content = [post_for_score("2015-2016", "1"),
                                 post_for_score("2014-2015", "1"), post_for_score("2014-2015", "2"),
                                 post_for_score("2015-2016", "2")]

            elif stu_id == "15":
                score_content = [post_for_score("2015-2016", "1"), post_for_score("2015-2016", "2")]

            else:
                return render_template("404.html")

            return render_template("main/zhengfang.html", stu_base_info=stu_base_info, class_info=class_info,
                                   score_content=score_content)

        except Exception:
            flash(u"帐号或密码错误")
            return redirect("zhengfang")
    else:
        return 'Sorry, you are not allowed to ask this page!'
