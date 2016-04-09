#!/usr/bin/env python
# coding=utf-8

import requests
from bs4 import BeautifulSoup

URL = 'http://210.44.176.116/cjcx/zcjcx_list.php'

def get_grade_list(studentno):
    data = {'post_xuehao': studentno}
    res = requests.post(URL, data=data)
    soup = BeautifulSoup(res.text)

    # 获得学生信息
    try:
        info = {
            'no': studentno,
            'name': soup.body.table.find_all('table')[0].find_all('tr')[1].find_all('td')[1].text,
            'class': soup.body.table.find_all('table')[0].find_all('tr')[1].find_all('td')[6].text
        }
    except:
        return None

    # 获得学生成绩单
    gradelist = []
    len = 0
    for grade in soup.body.table.find_all('table')[2].find_all('tr'):
        if len == 0:
            len += 1
            continue

        # 跳过双专业
        way = grade.find_all('td')[8].text.strip()
        if way.isalpha():
            continue

        tmp = {
            'id': grade.find_all('td')[0].text.strip(),
            'schoolyear': grade.find_all('td')[1].text.strip(),
            'semester': grade.find_all('td')[2].text.strip(),
            'class': grade.find_all('td')[3].text.strip(),
            'name': grade.find_all('td')[5].text.strip(),
            'point': grade.find_all('td')[7].text.strip(),
            'grade': grade.find_all('td')[9].text.strip()
        }

        update = grade.find_all('td')[10].text.strip()
        if update is not None and update.isdigit():
            tmp['grade'] = update

        gradelist.append(tmp)

    return {
        'info': info,
        'gradelist': gradelist
    }

