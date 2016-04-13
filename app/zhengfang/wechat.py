# -*- coding: utf-8 -*-

# 教务处成绩查询
from app import app
from flask import request, render_template, redirect, flash, url_for
from ..form import JwcForm
from bs4 import BeautifulSoup
from get_random_str import get_random_str
import urllib
import urllib2
import cookielib
from ..db_operating import User

get_view_state = ''
get_cookie = ''
wechat_id = {"wechat_id": ""}


def get_cookiejar():
    # 初始化一个CookieJar来处理Cookie
    cookiejar = cookielib.MozillaCookieJar()
    # 下面两行为了调试的
    httpHandler = urllib2.HTTPHandler(debuglevel=1)
    httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
    cookieSupport = urllib2.HTTPCookieProcessor(cookiejar)
    # 实例化一个全局opener
    opener = urllib2.build_opener(cookieSupport, httpHandler)
    urllib2.install_opener(opener)
    return cookiejar


@app.route('/wechat/building/zhengfang', methods=['GET', 'POST'])
def zhengfang_building():
    if request.method == 'POST':
        form = JwcForm()
        xh_post = form.number.data
        password_post = form.passwd.data
        check_code_post = form.check_code.data
        # print get_view_state, get_cookie
        postData = {
            '__VIEWSTATE': get_view_state,
            'txtUserName': xh_post,
            'TextBox2': password_post,
            'txtSecretCode': check_code_post,
            'RadioButtonList1': '%D1%A7%C9%FA',
            'Button1': '',
            'lbLanguage': '',
            'hidPdrs': '',
            'hidsc': ''
        }
        # post请求头部
        headers = {

            'Host': '210.44.176.46',
            'User-Agent': ' Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0 Iceweasel/38.5.0',
            'Accept': ' text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': ' zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding': ' gzip, deflate',
            'Referer': ' http://210.44.176.46/',
            'Cookie': get_cookie,
            'Connection': ' keep-alive'

        }
        default_url = 'http://210.44.176.46/default2.aspx'
        real_url = 'http://210.44.176.46/xs_main.aspx?xh=%s' % xh_post
        # print xh_post
        # print '###############\n\n###########\n\n%s' % xh_post
        postData = urllib.urlencode(postData)
        request1 = urllib2.Request(default_url, postData, headers)
        response1 = urllib2.urlopen(request1)
        soup = BeautifulSoup(response1.read(), 'html.parser', from_encoding='utf-8')
        span = soup.find_all("span", id="xhxm")

        try:
            print span[0].get_text().strip()
            info = User(stu_id=xh_post, wechat_id=wechat_id["wechat_id"], zhengfang_password=password_post,
                        library_password="")
            info.save()
            return redirect(url_for("wechat_library", xh_post=xh_post))
        except:
            flash(u"帐号或密码错误")
            return redirect(url_for("zhengfang_building"))

            # except Exception:
            # flash(u"帐号或密码错误")
            # return redirect(url_for("wechat/building/zhengfang"))

    else:
        wechat_id["wechat_id"] = request.args.get("token")
        flag = request.args.get("token")
        if flag != 'huiyang2333':
            return u"you are not allowed ti get this page"

        login_url = 'http://210.44.176.46/'
        cookiejar = get_cookiejar()
        LoginCookie = urllib2.urlopen(login_url)
        login_html = LoginCookie.read().decode('gbk')
        soup = BeautifulSoup(login_html, 'html5lib')
        global get_view_state
        view_state = soup.find_all("input")
        get_view_state = view_state[0].get('value')
        cookies = ''
        for index, cookie in enumerate(cookiejar):
            cookies = cookies + cookie.name + "=" + cookie.value + ";"
        global get_cookie
        get_cookie = cookies[:-1]
        random_str = get_random_str()

        # 验证码
        file = urllib2.urlopen("http://210.44.176.46/CheckCode.aspx")
        pic = file.read()
        path = '/home/lvhuiyang/check_code/%s.aspx' % random_str
        local_pic = open(path, "wb")
        local_pic.write(pic)
        local_pic.close()
        form = JwcForm()
        import base64
        f = open(r'/home/lvhuiyang/check_code/%s.aspx' % random_str, 'rb')
        ls_f = base64.b64encode(f.read())
        f.close()
        return render_template('wechat_building.html', form=form, ls_f=ls_f)
