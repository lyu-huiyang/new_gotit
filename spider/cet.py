# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

login_url = 'http://cet.redrock-team.com/'
post_url = 'http://cet.redrock-team.com/api/v2/basic'


def get_cet(name, number):
    data = {
        'name': name,
        'ticket': number
    }
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Connection': 'keep-alive',
        'Content-Length': '55',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'pgv_pvi=1855181824; pgv_si=s6883492864',
        'Host': 'cet.redrock-team.com',
        'Origin': 'http://cet.redrock-team.com',
        'Referer': 'http://cet.redrock-team.com/',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    post_page = requests.post(post_url, data=data, headers=headers)
    # print post_page.url
    # print post_page.encoding
    soup = BeautifulSoup(post_page.text, 'html.parser', from_encoding='utf-8')
    print soup
    text = str(soup).strip()
    # print type(text)
    text = eval(text)
    return text


if __name__ == '__main__':
    get_cet('孙艳军', '371012152119111')
