# -*- coding: utf-8 -*-
'''
一键绑定：系统检测到您已经绑定，无需重复绑定，如果需要更换绑定账号，请先解绑后再进行绑定
绑定界面。
查课表->已绑定进入数据库查课表，未绑定提示未绑定信息，并提示是否不绑定进行查询
查教务成绩
查绩点
查图书借阅情况
解除绑定：系统检测到您已经绑定，是否解除绑定？
系统检测到您并未绑定，所以不需要解绑，前去一键绑定？
使用说明：
'''
import time  # 用来记录生成微信消息的时间
import hashlib
import xml.etree.ElementTree as ET
from flask import render_template, request, url_for
from main.forms import *
from config import app, StuInfo, db
from spider.library import *
from spider.get_random_str import *
from spider.cet_no_number import *
import cookielib
import urllib2
import urllib

get_view_state = ''
get_cookie = ''
library_number = ''
library_password = ''
stu_info = {'stu_id': '', 'wechat_id': '', 'jwc_password': '', 'library_password': ''}


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


def check_if_binding(wechat_id):
    if StuInfo.query.filter_by(wechat_id=wechat_id).first() != None:
        return True
    else:
        return False


@app.route('/wechat', methods=['GET', 'POST'])  # 微信主页面
def wechat():
    if request.method == 'GET':
        if request.args.get('timestamp') == None:
            return u'对不起，您无权访问此界面'
        timestamp = request.args.get('timestamp')
        nonce = request.args.get('nonce')
        echostr = request.args.get('echostr')
        token = 'lvhuiyang'
        li = [token, timestamp, nonce]
        li.sort()
        sha1 = hashlib.sha1()
        map(sha1.update, li)
        hashcode = sha1.hexdigest()
        if hashcode == request.args.get('signature'):
            return echostr
        else:
            print "There is an error"
    else:
        print 'HelloWorld'
        message = request.data  # 接收用户消息
        root = ET.fromstring(message)  # 解析xml
        to_user_name = root.findall('ToUserName')[0].text  # 开发者账号
        from_user_name = root.findall('FromUserName')[0].text  # 用户微信id
        create_time = root.findall('CreateTime')[0].text  # 消息创建时间 （整型）
        message_type = root.findall('MsgType')[0].text  # 消息类型text
        content = root.findall('Content')[0].text  # 消息内容
        message_id = root.findall('MsgId')[0].text  # 消息的ID
        if content == u"一键绑定":
            if check_if_binding(from_user_name):  # 已经绑定的话返回的是true提示用户不需要再绑定了
                create_time = int(round(time.time() * 1000))
                return """<xml>
                <ToUserName><![CDATA[%s]]></ToUserName>
                <FromUserName><![CDATA[%s]]></FromUserName>
                <CreateTime>%s</CreateTime>
                <MsgType><![CDATA[text]]></MsgType>
                <Content><![CDATA[系统检测到您已经绑定，无需重复绑定，如果需要更换绑定账号，请先解绑后再进行绑定]]></Content>
                </xml>""" % (from_user_name, to_user_name, create_time)
            else:  # 用户没有绑定的话进入绑定界面，返回的图文消息
                create_time = int(round(time.time() * 1000))
                stu_info['wechat_id'] = from_user_name
                return """
                <xml>
                <ToUserName><![CDATA[%s]]></ToUserName>
                <FromUserName><![CDATA[%s]]></FromUserName>
                <CreateTime>%s</CreateTime>
                <MsgType><![CDATA[news]]></MsgType>
                <ArticleCount>1</ArticleCount>
                <Articles>
                <item>
                <Title><![CDATA[欢迎使用gotit]]></Title>
                <Description><![CDATA[系统检测到您并未绑定，点击此页面前去绑定。或者您并不想进行绑定，请点击菜单栏的‘无绑定查询’]]></Description>
                <Url><![CDATA[lvhuiyang.cn/wechat/building]]></Url>
                </item>
                </xml>
                """ % (from_user_name, to_user_name, create_time)
        elif content == u"查课表":
            pass
        elif content == u"查教务成绩":
            pass
        elif content == u"查绩点":
            pass
        elif content == u"图书借阅查询":
            return """
                <xml>
                <ToUserName><![CDATA[%s]]></ToUserName>
                <FromUserName><![CDATA[%s]]></FromUserName>
                <CreateTime>%s</CreateTime>
                <MsgType><![CDATA[news]]></MsgType>
                <ArticleCount>1</ArticleCount>
                <Articles>
                <item>
                <Title><![CDATA[欢迎使用gotit，图书借阅查询]]></Title>
                <Description><![CDATA[>>> 查看详细信息 <<<]]></Description>
                <Url><![CDATA[lvhuiyang.cn/wechat/library_info?wechat_id=%s]]></Url>
                </item>
                </xml>
                """ % (from_user_name, to_user_name, create_time, from_user_name)
        elif content == u"解除绑定":
            if check_if_binding(from_user_name):

                return """<xml>
                <ToUserName><![CDATA[%s]]></ToUserName>
                <FromUserName><![CDATA[%s]]></FromUserName>
                <CreateTime>%s</CreateTime>
                <MsgType><![CDATA[text]]></MsgType>
                <Content><![CDATA[解绑成功，您可以再次绑定，或者您不想进行绑定，请点击菜单栏的‘无绑定查询’]]></Content>
                </xml>""" % (from_user_name, to_user_name, create_time)
            else:
                return """<xml>
                <ToUserName><![CDATA[%s]]></ToUserName>
                <FromUserName><![CDATA[%s]]></FromUserName>
                <CreateTime>%s</CreateTime>
                <MsgType><![CDATA[text]]></MsgType>
                <Content><![CDATA[系统检测到您并没有绑定，所以无需进行此操作。]]></Content>
                </xml>""" % (from_user_name, to_user_name, create_time)
        else:
            pass


@app.route('/wechat/building', methods=['GET', 'POST'])  # 微信绑定页面
def building():
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
            stu_info['stu_id'] = xh_post
            stu_info['jwc_password'] = password_post
            return url_for('/wechat/library', xh_post=xh_post)

        except Exception:
            return render_template("jwc_error.html", message=u"密码或验证码错误，重新绑定")
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
        return render_template('wechat_building.html', form=form, ls_f=ls_f)


@app.route('/wechat/library', methods=['GET', 'POST'])
def wechat_library():
    form = LibraryBuilding()
    xh_post = request.args.get('xh_post')
    if request.method == 'GET':
        return render_template('wechat_library.html', form=form, xh_post=xh_post)
    else:
        password = form.password.data
        if check_login(xh_post, password).url == 'http://222.206.65.12/reader/book_lst.php':
            stu_info['library_password'] = password
            stu_id = StuInfo(stu_id=stu_info['stu_id'])
            wechat_id = StuInfo(wechat_id=stu_info['wechat_id'])
            jwc_password = StuInfo(jwc_password=stu_info['jwc_password'])
            library_password_ = StuInfo(library_password=stu_info['library_password'])
            db.session.add_all([stu_id, wechat_id, jwc_password, library_password_])
            db.session.commit()
            return render_template("building_successful.html", message=u"恭喜您，绑定成功，您可以实现一键查询了，祝您生活愉快")
        else:
            return render_template("jwc_error.html", message=u"帐号或密码错误,请重新绑定")


@app.route('/wechat/library_info', methods=['GET', 'POST'])
def wechat_library():
    if request.method == 'GET':
        if request.args.get('wechat_id') == None:
            return u'对不起，您无权访问此界面'
        else:
            wechat_id = request.args.get('wechat_id')
            number = StuInfo.query.filter_by(wechat_id=wechat_id).first()
            passwd = StuInfo.query.filter_by(wechat_id=wechat_id).first()
    pass
