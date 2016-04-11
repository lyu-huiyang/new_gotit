# coding=utf-8
# 教务处成绩查询
from app import app
from flask import request, render_template, redirect, flash
from ..form import JwcForm
from bs4 import BeautifulSoup
from get_random_str import get_random_str
import urllib
import urllib2
import cookielib

get_view_state = ''
get_cookie = ''


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


@app.route('/class', methods=['GET', 'POST'])
def zhengfang_class():
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

        headers2 = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Connection': 'keep-alive',
            'Cookie': get_cookie,
            'Host': '210.44.176.46',
            'Referer': real_url,
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36'
        }

        class_page = "http://210.44.176.46/xscjcx.aspx?xh=%s&xm=%r&gnmkdm=N121603" % (xh_post, password_post)
        class_ = 'http://210.44.176.46/xskbcx.aspx?xh=14110543055&xm=%C2%C0%BB%E6%D1%EE&gnmkdm=N121603'
        # print score_page
        postData2 = {
            'xh': xh_post,
            'xm': '',
            'gnmkdm': 'N121603'
        }
        request2 = urllib2.Request(class_, headers=headers2, data=postData2)
        response2 = urllib2.urlopen(request2)
        page_content = response2.read()
        soup = BeautifulSoup(page_content, "html5lib")
        try:
            stu_info = []
            stu_id = soup.find_all("span", id="Label5")[0].get_text().strip()
            stu_name = soup.find_all("span", id="Label6")[0].get_text().strip()
            stu_school = soup.find_all("span", id="Label7")[0].get_text().strip()
            stu_zhuanye = soup.find_all("span", id="Label8")[0].get_text().strip()
            stu_class = soup.find_all("span", id="Label9")[0].get_text().strip()

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
            class_10_list = []

            classes = soup.find_all("tr")

            for i1 in classes[4].find_all("td", width="7%"):
                print '12', i1.get_text().strip()
                class_12_list.append(i1.get_text().strip())

            for i2 in classes[6].find_all("td", align="Center"):
                class_34_list.append(i2.get_text().strip())
                print '34', i2.get_text().strip()

            for i in classes[8].find_all("td", align="Center"):
                class_56_list.append(i.get_text().strip())
                print '56', i.get_text().strip()

            for i in classes[10].find_all("td", align="Center"):
                class_78_list.append(i.get_text().strip())
                print '78', i.get_text().strip()

            for i in classes[12].find_all("td", align="Center"):
                class_9_list.append(i.get_text().strip())
                print '9', i.get_text().strip()

            for i in classes[13].find_all("td", align="Center"):
                class_10_list.append(i.get_text().strip())
                print '10', i.get_text().strip()

            all_classes.append(class_12_list)
            all_classes.append(class_34_list)
            all_classes.append(class_56_list)
            all_classes.append(class_78_list)
            all_classes.append(class_9_list)
            all_classes.append(class_10_list)

            return_info = []
            return_info.append(stu_info)
            return_info.append(all_classes)
            num = [12, 34, 56, 78, 9, 10]

            return render_template("class.html", return_info=return_info, num=num)
        except:
            flash(u"账号或密码错误")
            return redirect("class")



    else:
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
        path = 'D:\check_code\%s.aspx' % random_str
        local_pic = open(path, "wb")
        local_pic.write(pic)
        local_pic.close()
        form = JwcForm()
        import base64
        f = open(r'D:\check_code\%s.aspx' % random_str, 'rb')
        ls_f = base64.b64encode(f.read())
        f.close()
        return render_template('class_login.html', form=form, ls_f=ls_f)
