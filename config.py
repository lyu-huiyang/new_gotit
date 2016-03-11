# -*- coding: utf-8 -*-
"""
The flask application package.
"""

from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = "hard to guess string"

import main.views