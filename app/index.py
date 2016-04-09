# -*- coding: utf-8 -*-
from datetime import datetime
from flask import render_template
from . import app


@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title=u'主页',
        year=datetime.now().year,
    )


@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title=u'联系我们',
        year=datetime.now().year,
        message1=u'山东理工大学Linux用户组',
        message2=u'山东理工大学报',
        connection=u'如果您发现bug请联系：'
    )


@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title=u'关于本站',
        year=datetime.now().year,
        message=u'山东理工大学信息一站式查询系统'
    )


@app.route('/notice')
def notice():
    return render_template('notice.html')
