# coding=utf-8
# 教务处成绩查询
from app import app
from flask import request, render_template,redirect,flash
from ..form import JwcForm
from bs4 import BeautifulSoup
from get_random_str import get_random_str
import urllib
import urllib2
import cookielib
from ..db_operating import get_coll

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


@app.route('/zhengfang_no_input_query', methods=['GET', 'POST'])
def zhengfang_no_input_query():
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
            flash(u"帐号或密码错误")
            return redirect("zhengfang")

    else:
        wechat_id = request.args.get('wechat_id')
        db = get_coll()
        a = db.users.find({"wechat_id": wechat_id}, {"wechat_id": 1, "_id": 0})
        for i in a:
            number = i['stu_id']
            passwd = i['library_password']
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
        return render_template('jwc_login.html', ls_f=ls_f, number=number,passwd=passwd)