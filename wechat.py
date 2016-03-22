# -*- coding: utf-8 -*-
from flask import Flask, request, make_response
import xml.etree.ElementTree as ET
import hashlib

app = Flask(__name__)
from wechat_sdk import WechatConf

conf = WechatConf(
    token='lvhuiyang',
    appid='wx35028b78608d38f9',
    appsecret='107da9b468d3cf7427dc439de6405d01',
)

from wechat_sdk import WechatBasic

wechat = WechatBasic(conf=conf)


@app.route('/wechat')
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
        '''
        if hashcode == request.args.get('signature'):
            return echostr
        else:
            print "There is an error"'''
        if wechat.check_signature(hashcode, timestamp, nonce):
            print 'Accept'
        else:
            print 'Wrong'
    elif request.method == 'POST':
        print 'HelloWorld'
        rec = request.stream.read()
        xml_rec = ET.fromstring(rec)
        print '###############', xml_rec
        fromu = xml_rec.find('FromUserName').text
        event = xml_rec.find('Event')
        event_key = xml_rec.find('EventKey')
        content = xml_rec.find('Content')
    else:
        pass


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=80)
