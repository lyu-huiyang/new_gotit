# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

login_url = 'http://cet.redrock-team.com/'
post_url = 'http://cet.redrock-team.com/api/v2/noticket'


def get_cet(name, cet_type):
    data = {
        'name': name,
        'school': '山东理工大学',
        'cetType': cet_type
    }
    post_page = requests.post(post_url, data=data)
    print post_page.url
    print post_page.encoding
    soup = BeautifulSoup(post_page.text, 'html.parser', from_encoding='utf-8')
    print soup
    text = str(soup)
    print type(text)
    text = eval(text)
    return text


if __name__ == '__main__':
    get_cet('吕绘杨','1')
