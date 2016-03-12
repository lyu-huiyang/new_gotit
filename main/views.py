# -*- coding: utf-8 -*-
"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, flash, request, redirect, url_for
from forms import *
from config import app
from spider.library import *
from spider.score import *
from spider.get_random_str import *
from spider.cet import *
from spider.cet_no_number import *
import cookielib
import urllib2
import urllib

get_view_state = ''
get_cookie = ''
library_number = ''
library_password = ''


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


@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title=u'主页',
        year=datetime.now().year,
    )


@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title=u'联系我们',
        year=datetime.now().year,
        message1=u'山东理工大学Linux用户组',
        message2=u'山东理工大学报',
        connection=u'如果您发现bug请联系：'
    )


@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title=u'关于本站',
        year=datetime.now().year,
        message=u'山东理工大学信息一站式查询系统'
    )


@app.route('/notice')
def notice():
    return render_template('notice.html')


# 综合成绩查询视图函数
@app.route('/score', methods=['GET', 'POST'])
def score():
    form = ScoreForm()
    if form.validate_on_submit():
        post_xuehao = form.post_xuehao.data
        if len(check_score(post_xuehao)) > 10:
            return_data = score_login(post_xuehao)
            return render_template('score.html', return_data=return_data)
        else:
            flash(u'请输入正确的学号')
    return render_template('score_login.html', form=form)


# 图书馆成绩查询视图函数
@app.route('/library', methods=['GET', 'POST'])
def library():
    form = LibraryForm()
    if form.is_submitted():
        number = form.number.data
        passwd = form.passwd.data
        # global library_number, library_password
        # library_number = number
        # library_password = passwd
        if check_login(number, passwd).url == 'http://222.206.65.12/reader/book_lst.php':
            books = library_login(number, passwd)
            return render_template('library.html', books=books, number=number, passwd=passwd)
        else:
            flash(u'帐号或密码错误')
    return render_template('library_login.html', form=form)


# 图书馆借阅历史查询
@app.route('/library_history', methods=['GET', 'POST'])
def book_history():
    if request.method == 'POST':
        number = request.form['number']
        passwd = request.form['pass']
        books = library_history(number,passwd)
        return render_template('book_history.html', books=books)


@app.route('/cet', methods=['GET', 'POST'])
def cet():
    form = CetForm()
    if form.is_submitted():
        name = form.name.data
        ticket = form.number.data
        info = get_cet(name, ticket)
        if info['status'] == '0':
            return_info = info
            return render_template('cet.html', return_info=return_info)
        else:
            flash(u'请输入正确的准考证号以及姓名')
    return render_template('cet_login.html', form=form)


@app.route('/cet_no_number', methods=['GET', 'POST'])
def cet_no_number():
    return render_template('cet_no_number_login.html')


# 教务处成绩查询
@app.route('/jwc', methods=['GET', 'POST'])
def jwc():
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
        try:

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

            score_page = "http://210.44.176.46/xscjcx.aspx?xh=%s&xm=%r&gnmkdm=N121605" % (xh_post, password_post)
            # print score_page
            request2 = urllib2.Request(score_page, headers=headers2)
            response2 = urllib2.urlopen(request2)
            page_content = response2.read()
            soup = BeautifulSoup(page_content, 'html.parser', from_encoding='utf-8')
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
                headers2['Referer'] = score_page
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
                postData2 = urllib.urlencode(postData2)
                request3 = urllib2.Request(score_page, postData2, headers=headers2)
                response3 = urllib2.urlopen(request3)
                page_content = response3.read().decode('gbk')
                # print(page_content)
                soup = BeautifulSoup(page_content, 'html.parser', from_encoding="utf-8")
                data_list = soup.find_all("td")
                # print data_list, soup
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
                                 post_for_score("2013-2014", "1"), post_for_score("2013-2014", "2")]

            elif stu_id == "14":
                score_content = [post_for_score("2015-2016", "1"),
                                 post_for_score("2014-2015", "1"), post_for_score("2014-2015", "2")]

            elif stu_id == "15":
                score_content = [post_for_score("2015-2016", "1")]

            else:
                return render_template("404.html")

            return render_template("jwc.html", stu_base_info=stu_base_info, class_info=class_info,
                                   score_content=score_content)

        except Exception:
            return render_template("jwc_error.html", message=u"帐号或密码错误")

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
        path = '/home/lvhuiyang/check_code/%s.aspx' % random_str
        local_pic = open(path, "wb")
        local_pic.write(pic)
        local_pic.close()
        form = JwcForm()
        import base64
        f = open(r'/home/lvhuiyang/check_code/%s.aspx' % random_str, 'rb')
        ls_f = base64.b64encode(f.read())
        f.close()
        return render_template('jwc_login.html', form=form, ls_f=ls_f)
