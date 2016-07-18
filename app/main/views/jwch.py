# coding=utf-8
from flask import render_template
from flask import request
from flask import session
from bs4 import BeautifulSoup
from .. import main
import copy
import requests

# 教务综合成绩查询页面内容
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


def get_student(studentno):
    gradelist = get_grade_list(studentno)
    if gradelist is None:
        return None
    pointinfo = computer(gradelist)
    return {
        'gradelist': gradelist,
        'pointinfo': pointinfo
    }


def computer(gradelist):
    sumgrade = 0.0
    sumpoint = 0.0
    pointinfo = {}

    for g in gradelist['gradelist']:
        if g['class'] != u'公选课':
            gradetmp = __score2number(g['grade'])
            if gradetmp < 60:
                gradetmp = 0.0

            pointtmp = float(g['point'])
            sumgrade += gradetmp * pointtmp
            if g['name'] not in pointinfo:
                sumpoint += pointtmp
                pointinfo[g['name']] = gradetmp
            else:
                if gradetmp > pointinfo[g['name']]:
                    sumgrade -= pointinfo[g['name']] * pointtmp
                    pointinfo[g['name']] = gradetmp

    pointinfo['sumgrade'] = sumgrade
    pointinfo['sumpoint'] = sumpoint
    pointinfo['point'] = sumgrade / sumpoint

    return pointinfo


def __score2number(text):
    '''将二级和五级成绩转换成数字成绩,或者将成绩转换成浮点型'''
    sc_dict = {
        u'合格': 70,
        u'不合格': 0,
        u'优秀': 95,
        u'良好': 84,
        u'中等': 73,
        u'及格': 62,
        u'不及格': 0,
        u'缺考': 0,
        u'禁考': 0,
        u'退学': 0,
        u'缓考（时': 0,
        u'缓考': 0,
        u'休学': 0,
        u'未选': 0,
        u'作弊': 0,
        u'取消': 0,
        u'免修': 60,
        u'优': 95,
        u'良': 84,
        u'中': 73,
        u'-': 0,
        u'': 0
    }
    try:
        num = sc_dict[text]
        return num
    except:
        try:
            num = float(text)
            return num
        except:
            return 0


@main.route('/find')
def find():
    return render_template('main/find.html')


@main.route('/list', methods=['POST'])
def ans():
    if request.method == 'POST':
        student = request.form['number']

        if student.isdigit():
            studentinfo = get_student(student)
            if studentinfo is not None:
                # 加入session
                session['user'] = studentinfo['gradelist']
                return render_template(
                    'main/ans.html',
                    info=studentinfo['gradelist'],
                    point=studentinfo['pointinfo']
                )

    return render_template('main/find.html')


@main.route('/update', methods=['POST'])
def update():
    if request.method == 'POST':
        # student = request.form['no']
        gradelist = copy.deepcopy(session['user'])
        len = 1
        for grade in gradelist['gradelist']:
            grade['grade'] = request.form['c' + str(len)]
            len += 1

        gradelist = computer(gradelist)
        return render_template(
            'main/ans.html',
            info=session['user'],
            point=gradelist
        )

    return render_template('main/find.html')
