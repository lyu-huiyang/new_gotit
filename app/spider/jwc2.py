# -*- coding: utf-8 -*-
import urllib
import urllib2
import cookielib
from bs4 import BeautifulSoup


def get_jwc_cookie():
    login_url = 'http://210.44.176.46/'
    # 初始化一个CookieJar来处理Cookie
    cookiejar = cookielib.MozillaCookieJar()
    httpHandler = urllib2.HTTPHandler(debuglevel=1)
    httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
    cookieSupport = urllib2.HTTPCookieProcessor(cookiejar)
    opener = urllib2.build_opener(cookieSupport, httpsHandler)
    urllib2.install_opener(opener)
    # 获取cookie
    LoginCookie = urllib2.urlopen(login_url)
    login_html = LoginCookie.read().decode('gbk')
    soup = BeautifulSoup(login_html, 'html5lib')
    view_state = soup.find_all("input")
    view_state = view_state[0].get('value')
    cookies = ''
    for index, cookie in enumerate(cookiejar):
        cookies = cookies + cookie.name + "=" + cookie.value + ";"
    cookie = cookies[:-1]
    cookie_and_state = [cookie, view_state]
    return cookie_and_state


def jwc_check_if_login(number, password, check_code, cookie, view_state):
    # 请求数据
    postData = {
        '__VIEWSTATE': view_state,
        'txtUserName': number,
        'TextBox2': password,
        'txtSecretCode': check_code,
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
        'Cookie': cookie,
        'Connection': ' keep-alive'

    }
    default_url = 'http://210.44.176.46/default2.aspx'
    postData = urllib.urlencode(postData)
    request = urllib2.Request(default_url, postData, headers)
    response = urllib2.urlopen(request)
    cur_url = response.geturl()
    return cur_url


def jwc_login(number, password, check_code):
    pass


def query_score(year, term):
    pass
