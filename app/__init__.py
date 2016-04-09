# -*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard_to_guess_string'

import index
import jwc
import library
import zhengfang
import zhengfang_class
