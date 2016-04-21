# -*- coding: utf-8 -*-
from flask import Flask
from werkzeug.contrib.fixers import ProxyFix

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard_to_guess_string'

import index
import jwc
import library
import zhengfang
import zhengfang_class
import wechat_index

app.wsgi_app = ProxyFix(app.wsgi_app)
