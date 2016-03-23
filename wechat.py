# -*- coding: utf-8 -*-
from flask import request
import hashlib
import xml.etree.ElementTree as ET

from config import app


@app.route('/wechat', methods=['GET', 'POST'])
def wechat():
    if request.method == 'GET':
        timestamp = request.args.get('timestamp')
        nonce = request.args.get('nonce')
        echostr = request.args.get('echostr')
        token = 'lvhuiyang'
        li = [token, timestamp, nonce]
        li.sort()
        sha1 = hashlib.sha1()
        map(sha1.update, li)
        hashcode = sha1.hexdigest()
        if hashcode == request.args.get('signature'):
            return echostr
        else:
            print "There is an error"
    else:
        print 'HelloWorld'
        message = request.data  # get the data from post request
        root = ET.fromstring(message)
        to_user_name = root.findall('ToUserName')[0].text
        from_user_name = root.findall('FromUserName')[0].text
        create_time = root.findall('CreateTime')[0].text
        message_type = root.findall('MsgType')[0].text
        content = root.findall('Content')[0].text
        if content == "综合成绩查询":
            pass
        message_id = root.findall('MsgId')[0].text
        return_message = """<xml>
        <ToUserName><![CDATA[%s]]></ToUserName>
        <FromUserName><![CDATA[%s]]></FromUserName>
        <CreateTime>%s</CreateTime>
        <MsgType><![CDATA[%s]]></MsgType>
        <Content><![CDATA[%s]]></Content>
        </xml>""" % (from_user_name, to_user_name, create_time, message_type, content)
        return return_message


