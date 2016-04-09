#!/usr/bin/env python
# coding=utf-8
import spider

def get_student(studentno):
    gradelist = spider.get_grade_list(studentno)

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
    sc_dict={
        u'合格':70,
        u'不合格':0,
        u'优秀':95,
        u'良好':84,
        u'中等':73,
        u'及格':62,
        u'不及格':0,
        u'缺考':0,
        u'禁考':0,
        u'退学':0,
        u'缓考（时':0,
        u'缓考':0,
        u'休学':0,
        u'未选':0,
        u'作弊':0,
        u'取消':0,
        u'免修':60,
        u'优':95,
        u'良':84,
        u'中':73,
        u'-':0,
        u'':0
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
