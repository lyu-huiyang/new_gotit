# -*- coding: utf-8 -*-
# from config import app
from flask import Flask, request
import hashlib

app = Flask(__name__)


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

        if hashcode == request.args.get('signature'):
            return echostr
        else:
            print "There is an error"
    elif request.method == 'POST':
        post_body = request.data
        print post_body
    else:
        pass


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=80)
