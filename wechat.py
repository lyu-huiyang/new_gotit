# -*- coding: utf-8 -*-
# from config import app
from flask import Flask, request

from wechat_sdk import WechatBasic
from wechat_sdk import WechatConf
import hashlib

conf = WechatConf(
    token='lvhuiyang',
    appid='wx35028b78608d38f9',
    appsecret='107da9b468d3cf7427dc439de6405d01',
    # encrypt_mode='safe',  # 可选项：normal/compatible/safe，分别对应于 明文/兼容/安全 模式
    # encoding_aes_key='your_encoding_aes_key'  # 如果传入此值则必须保证同时传入 token, appid
)

app = Flask(__name__)
wechat = WechatBasic(conf=conf)

# 微信开发
@app.route('/wechat')
def wechat():
    timestamp = request.args('timestamp')
    nonce = request.args('nonce')
    echostr = request.args('echostr')
    token = 'lvhuiyang'
    li = [token, timestamp, nonce]
    li.sort()
    sha1 = hashlib.sha1()
    map(sha1.update, li)
    hashcode = sha1.hexdigest()

    if hashcode == request.args('signature'):
        return echostr
    else:
        print "There is an error"


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=80)
