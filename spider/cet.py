# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import urllib2
import urllib
import cookielib




login_url = 'http://www.chsi.com.cn/cet/'


def get_cet(xkzh, xm):
    data = {
        "xkzh": xkzh,
        "xm": xm
    }
    data_url = 'http://www.chsi.com.cn/cet/query?xkzh=%r&xm=%r' % (xkzh, xm)
    # 初始化一个CookieJar来处理Cookie
    cookiejar = cookielib.MozillaCookieJar()
    # 下面两行为了调试的
    httpHandler = urllib2.HTTPHandler(debuglevel=1)
    httpsHandler = urllib2.HTTPSHandler(debuglevel=1)

    cookieSupport = urllib2.HTTPCookieProcessor(cookiejar)
    # 实例化一个全局opener
    opener = urllib2.build_opener(cookieSupport, httpsHandler)
    urllib2.install_opener(opener)
    LoginCookie = urllib2.urlopen(login_url)
    cookies = ''
    for index, cookie in enumerate(cookiejar):
        cookies = cookies + cookie.name + "=" + cookie.value + ";"

    # cookie = cookies[:-1]
    cookie = 'JSESSIONID=EB508D618986EAFDFF1656B8AD5972F8; __utmt=1; __utma=65168252.415852182.1456765913.1457550058.1457707028.3; __utmb=65168252.21.10.1457707028; __utmc=65168252; __utmz=65168252.1457707028.3.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic'
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Connection': 'keep-alive',
        'Cookie': cookie,
        'Host': 'www.chsi.com.cn',
        'Referer': 'http://www.chsi.com.cn/cet/',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1'

    }
    postData = urllib.urlencode(data)
    get_request = urllib2.Request(data_url, data=postData, headers=headers)
    response = urllib2.urlopen(get_request)
    # cur_url = response.geturl()
    page_content = response.read()
    print page_content


if __name__ == '__main__':
    get_cet('371012152119115', '吕绘杨')
