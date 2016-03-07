# coding: utf-8
import requests
from bs4 import BeautifulSoup


def check_score(post_xuehao):
    data = {'post_xuehao': post_xuehao}
    url = 'http://210.44.176.116/cjcx/zcjcx_list.php'
    res = requests.post(url, data=data, timeout=5.0)
    print res.encoding
    soup = BeautifulSoup(res.text, 'html.parser', from_encoding='utf-8')
    html_td = soup.find_all('td', scope="col")
    return html_td


def score_login(post_xuehao):
    data = {'post_xuehao': post_xuehao}
    url = 'http://210.44.176.116/cjcx/zcjcx_list.php'
    res = requests.post(url, data=data, timeout=5.0)
    print res.encoding
    soup = BeautifulSoup(res.text, 'html.parser', from_encoding='utf-8')
    html_td = soup.find_all('td', scope="col")
    # 学生个人信息 .strip()方法消除字符串中的空格
    student = {}
    student['number'] = html_td[0].get_text().strip()
    student['name'] = html_td[1].get_text().strip()
    student['sex'] = html_td[2].get_text().strip()
    student['year'] = html_td[3].get_text().strip()
    student['school'] = html_td[4].get_text().strip()
    student['major'] = html_td[5].get_text().strip()  # 专业
    student['the_class'] = html_td[6].get_text().strip()
    student['kind'] = html_td[7].get_text().strip()
    student['level'] = html_td[8].get_text().strip()
    student['length'] = html_td[9].get_text().strip()
    student['normal'] = html_td[10].get_text().strip()  # 师范
    student['language'] = html_td[11].get_text().strip()
    student['note'] = html_td[12].get_text().strip()

    # 课程信息
    temp_info = {}
    score_info = []
    k = 15
    for j in range(0, (len(html_td) - 16) / 14):  # 一共的课程数

        temp_info['number'] = html_td[k].get_text().strip()  # 序号
        temp_info['learn_year'] = html_td[k + 1].get_text().strip()  # 学年
        temp_info['term'] = html_td[k + 2].get_text().strip()  # 学期
        temp_info['class_kind'] = html_td[k + 3].get_text().strip()  # 类别
        temp_info['class_number'] = html_td[k + 4].get_text().strip()  # 课程编号
        temp_info['class_name'] = html_td[k + 5].get_text().strip()  # 课程名称
        temp_info['learn_time'] = html_td[k + 6].get_text().strip()  # 学时
        temp_info['credit'] = html_td[k + 7].get_text().strip()  # 学分
        temp_info['exam_way'] = html_td[k + 8].get_text().strip()  # 考核方式
        temp_info['first_point'] = html_td[k + 9].get_text().strip()  # 原来考试成绩
        temp_info['second_point'] = html_td[k + 10].get_text().strip()  # 补考成绩
        temp_info['grade_point'] = html_td[k + 11].get_text().strip()  # 课程绩点
        temp_info['credit_point'] = html_td[k + 12].get_text().strip()  # 学分绩点
        temp_info['teacher'] = html_td[k + 13].get_text().strip()  # 教师 k=28
        k += 14
        score_info.append(temp_info)
        temp_info = {}

    all_info = [student, score_info]

    return all_info


if __name__ == '__main__':
    a = check_score('14110543055')
