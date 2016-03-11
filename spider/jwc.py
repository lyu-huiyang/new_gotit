# -*- coding: utf-8 -*-
import urllib
import urllib2
import cookielib
from bs4 import BeautifulSoup

user_name = '14110543055'
password = 'LHy110114230'

login_url = 'http://210.44.176.46/'
check_code_url = 'http://210.44.176.46/CheckCode.aspx'
default_url = 'http://210.44.176.46/default2.aspx'
real_url = 'http://210.44.176.46/xs_main.aspx?xh=%s' % user_name

# 初始化一个CookieJar来处理Cookie
cookiejar = cookielib.MozillaCookieJar()
# 下面两行为了调试的
httpHandler = urllib2.HTTPHandler(debuglevel=1)
httpsHandler = urllib2.HTTPSHandler(debuglevel=1)

cookieSupport = urllib2.HTTPCookieProcessor(cookiejar)
# 实例化一个全局opener
opener = urllib2.build_opener(cookieSupport, httpsHandler)
urllib2.install_opener(opener)
# 获取cookie
LoginCookie = urllib2.urlopen(login_url)
login_html = LoginCookie.read().decode('gbk')
soup = BeautifulSoup(login_html, 'html5lib')
view_state = soup.find_all("input")
view_state = view_state[0].get('value')

# 验证码
file = urllib2.urlopen(check_code_url)
pic = file.read()
path = '/home/lvhuiyang/check_code/code.aspx'
local_pic = open(path, "wb")
local_pic.write(pic)
local_pic.close()
print "please  %s,open code.jpg" % path
text = raw_input("input code :")
print text

cookies = ''
for index, cookie in enumerate(cookiejar):
    cookies = cookies + cookie.name + "=" + cookie.value + ";"

cookie = cookies[:-1]
print '###############\nThis is cookie:\n\n', cookie, '\n\n'


# 请求数据
postData = {
    '__VIEWSTATE': view_state,
    'txtUserName': user_name,
    'TextBox2': password,
    'txtSecretCode': text,
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

postData = urllib.urlencode(postData)
request = urllib2.Request(default_url, postData, headers)
response = urllib2.urlopen(request)
cur_url = response.geturl()
print "curl-------------------",cur_url
page_content = response.read().decode('gbk')
# print '\n\n######################\n\n', page_content

soup = BeautifulSoup(page_content, 'html5lib')
soup_a = soup.find_all('a')
soup_span = soup.find_all('span', id="xhxm")
xm = soup_span[0].get_text().strip()
xm_post = xm[0:-2]

headers2 = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Connection': 'keep-alive',
    'Cookie': cookie,
    'Host': '210.44.176.46',
    'Referer': real_url,
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36'
}

score_page = "http://210.44.176.46/xscjcx.aspx?xh=%s&xm=%r&gnmkdm=N121605" % (user_name, xm_post)
print score_page
request = urllib2.Request(score_page, headers=headers2)
response = urllib2.urlopen(request)
page_content = response.read()
soup = BeautifulSoup(page_content, 'html5lib')

soup_input = soup.find_all("input")
score_view_state = soup_input[2].get('value')
print soup.find_all("span")



headers2['Referer'] = score_page

postData2 = {
    '__EVENTTARGET': '',
    '__EVENTARGUMENT': '',
    '__VIEWSTATE': score_view_state,
    'hidLanguage': '',
    'ddlXN': '2014-2015',
    'ddlXQ': '1',
    'ddl_kcxz': '',
    'btn_xq': ''
}
postData2 = urllib.urlencode(postData2)
request = urllib2.Request(score_page, postData2, headers=headers2)
response = urllib2.urlopen(request)
page_content = response.read().decode('gbk')
# print(page_content)
soup = BeautifulSoup(page_content, 'html.parser', from_encoding="utf-8")
data_list = soup.find_all("td")
print data_list, soup
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
    temp['second_point'] = data_list[count + 11].get_text().strip()  # 重修成绩
    temp['school'] = data_list[count + 12].get_text().strip()  # 学院
    temp['comment'] = data_list[count + 13].get_text().strip()  # 备注
    temp['second_flag'] = data_list[count + 14].get_text().strip()  # 重修标记
    return_data.append(temp)
    temp = {}
    count += 15
for j in return_data:
    print j