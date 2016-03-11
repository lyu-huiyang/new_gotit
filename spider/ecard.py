# -*- coding: utf-8 -*-
import urllib
import urllib2
import cookielib
from bs4 import BeautifulSoup

user_name = '14110543055'
user_password = '230916'

ecard_url = 'http://ecard.sdut.edu.cn/'
user_login_url = 'http://ecard.sdut.edu.cn/UserInfo/UserLogin.aspx'
check_code_url = 'http://ecard.sdut.edu.cn/Other/pic.aspx'
verify_url = 'http://ecard.sdut.edu.cn/EcardInfo/UserBaseInfo_Seach.aspx'
button_url = 'http://ecard.sdut.edu.cn/Index_button.aspx'
check_url1 = 'http://ecard.sdut.edu.cn/WebResource.axd?d=eY9T7q3HIgfevDeZ2I3HFI0cY9Lpo4lkNOShxVyLKG4ht3vG3UaMVzbHf53lBESN7zSJ5oPsnAp7-l737IwKo9188ws1&t=634604713351482412'
check_url2 = 'http://ecard.sdut.edu.cn/WebResource.axd?d=D7b7QxO3Ka7cgjoF-9CqLYFYDIHhUEa8zrBskTUe2hVd-24pURQHcs1phSV486QNTm4lTlKLVWCqwd9glKegZiPSLYE1&t=634604713351482412'
# 初始化一个CookieJar来处理Cookie
cookiejar = cookielib.MozillaCookieJar()
print '1_1'
# 下面两行为了调试的
cookieSupport = urllib2.HTTPCookieProcessor(cookiejar)
# 实例化一个全局opener
opener = urllib2.build_opener(cookieSupport)
urllib2.install_opener(opener)
# 获取cookie
print '112'
login_cookie = urllib2.urlopen(user_login_url)
print '1122'
#temp1 = urllib2.urlopen(check_url1)
#temp2 = urllib2.urlopen(check_url2)
login_cookie = login_cookie.read().decode('gbk')


file = urllib2.urlopen(check_code_url)
pic = file.read()
path = '/home/lvhuiyang/check_code/ecard_code.jpeg'
local_pic = open(path, "wb")
local_pic.write(pic)
local_pic.close()
print "please  %s,open ecard_code.jpeg" % path
text = raw_input("input code :")
print text

cookies = ''
for index, cookie in enumerate(cookiejar):
    cookies = cookies + cookie.name + "=" + cookie.value + ";"

cookie = cookies[:-1]
print "cookies:", cookie
soup = BeautifulSoup(login_cookie, 'html.parser', from_encoding="utf-8")
# print soup
__EVENTVALIDATION = soup.find_all("input", id="__EVENTVALIDATION")
__VIEWSTATE = soup.find_all("input", id="__VIEWSTATE")
__EVENTVALIDATION = __EVENTVALIDATION[0].get('value')
__VIEWSTATE = __VIEWSTATE[0].get('value')

post_data = {
    '__EVENTARGUMENT': '',
    '__EVENTTARGET': '',
    '__EVENTVALIDATION': __EVENTVALIDATION,
    '__VIEWSTATE': __VIEWSTATE,
    'txtUserName': user_name,
    'txtPwd': user_password,
    'btnUserLogin': '',
    'txtCheckCode': text
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Connection': 'keep-alive',
    'Cookie': cookie,
    'Host': 'ecard.sdut.edu.cn',
    'Referer': button_url,
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0 Iceweasel/38.5.0'
}
post_data = urllib.urlencode(post_data)
request = urllib2.Request(user_login_url, data=post_data, headers=headers)
response = urllib2.urlopen(request)
cur_url = response.geturl()
print cur_url
headers['Referer'] = user_login_url
request = urllib2.Request(verify_url, headers=headers)
response = urllib2.urlopen(request)
print(response.geturl())
page_content = response.read()
soup = BeautifulSoup(page_content, 'html.parser', from_encoding='gb18030')
print soup.originalEncoding
print soup.prettify()

