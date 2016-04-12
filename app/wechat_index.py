# -*- coding: utf-8 -*-
from app import app
from flask import request, render_template, url_for, flash
import time  # 用来记录生成微信消息的时间
import hashlib
import xml.etree.ElementTree as ET
from db_operating import User

'''
一键绑定：系统检测到您已经绑定，无需重复绑定，如果需要更换绑定账号，请先解绑后再进行绑定
绑定界面。
查课表->已绑定进入数据库查课表，未绑定提示未绑定信息，并提示是否不绑定进行查询
查教务成绩
查绩点
查图书借阅情况
解除绑定：系统检测到您已经绑定，是否解除绑定？
系统检测到您并未绑定，所以不需要解绑，前去一键绑定？
使用说明：
'''


@app.route('/wechat', methods=['GET', 'POST'])  # 微信主页面
def wechat():
    if request.method == 'GET':
        if request.args.get('timestamp') == None:
            return u'对不起，您无权访问此界面'
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
    elif request.method == 'POST':
        message = request.data  # 接收用户消息
        root = ET.fromstring(message)  # 解析xml
        to_user_name = root.findall('ToUserName')[0].text  # 开发者账号
        from_user_name = root.findall('FromUserName')[0].text  # 用户微信id
        create_time = root.findall('CreateTime')[0].text  # 消息创建时间 （整型）
        message_type = root.findall('MsgType')[0].text  # 消息类型text
        content = root.findall('Content')[0].text  # 消息内容
        message_id = root.findall('MsgId')[0].text  # 消息的ID
        if content == u"一键绑定":
            if User.check_if_binding(from_user_name):  # 已经绑定的话返回的是true提示用户不需要再绑定了
                create_time = int(round(time.time() * 1000))
                return """<xml>
                <ToUserName><![CDATA[%s]]></ToUserName>
                <FromUserName><![CDATA[%s]]></FromUserName>
                <CreateTime>%s</CreateTime>
                <MsgType><![CDATA[text]]></MsgType>
                <Content><![CDATA[系统检测到您已经绑定，无需重复绑定，如果需要更换绑定账号，请先解绑后再进行绑定]]></Content>
                </xml>""" % (from_user_name, to_user_name, create_time)
            else:  # 用户没有绑定的话进入绑定界面，返回的图文消息
                create_time = int(round(time.time() * 1000))
                return """
                <xml>
                <ToUserName><![CDATA[%s]]></ToUserName>
                <FromUserName><![CDATA[%s]]></FromUserName>
                <CreateTime>%s</CreateTime>
                <MsgType><![CDATA[news]]></MsgType>
                <ArticleCount>1</ArticleCount>
                <Articles>
                <item>
                <Title><![CDATA[欢迎使用gotit]]></Title>
                <Description><![CDATA[系统检测到您并未绑定，点击此页面前去绑定。或者您并不想进行绑定，请点击菜单栏的‘无绑定查询’]]></Description>
                <Url><![CDATA[lvhuiyang.cn/wechat/building/zhengfang?token=huiyang2333&wechat_id=%s]]></Url>
                </item>
                </xml>
                """ % (from_user_name, to_user_name, create_time, from_user_name)
        elif content == u"查课表":
            pass
        elif content == u"查教务成绩":
            pass
        elif content == u"查绩点":
            pass
        elif content == u"图书借阅查询":
            return """
                <xml>
                <ToUserName><![CDATA[%s]]></ToUserName>
                <FromUserName><![CDATA[%s]]></FromUserName>
                <CreateTime>%s</CreateTime>
                <MsgType><![CDATA[news]]></MsgType>
                <ArticleCount>1</ArticleCount>
                <Articles>
                <item>
                <Title><![CDATA[欢迎使用gotit，图书借阅查询]]></Title>
                <Description><![CDATA[>>> 查看详细信息 <<<]]></Description>
                <Url><![CDATA[lvhuiyang.cn/wechat/library_info?wechat_id=%s]]></Url>
                </item>
                </xml>
                """ % (from_user_name, to_user_name, create_time, from_user_name)
        elif content == u"解除绑定":
            if User.check_if_binding(from_user_name):
                User.cancel_building(from_user_name)
                return """<xml>
                <ToUserName><![CDATA[%s]]></ToUserName>
                <FromUserName><![CDATA[%s]]></FromUserName>
                <CreateTime>%s</CreateTime>
                <MsgType><![CDATA[text]]></MsgType>
                <Content><![CDATA[解绑成功，您可以再次绑定，或者您不想进行绑定，请点击菜单栏的‘无绑定查询’]]></Content>
                </xml>""" % (from_user_name, to_user_name, create_time)
            else:
                return """<xml>
                <ToUserName><![CDATA[%s]]></ToUserName>
                <FromUserName><![CDATA[%s]]></FromUserName>
                <CreateTime>%s</CreateTime>
                <MsgType><![CDATA[text]]></MsgType>
                <Content><![CDATA[系统检测到您并没有绑定，所以无需进行此操作。]]></Content>
                </xml>""" % (from_user_name, to_user_name, create_time)
        else:
            return u"请求非法"
    else:
        return u"请求非法"
