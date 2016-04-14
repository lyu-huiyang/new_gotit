#!/usr/bin/env python
# coding=utf-8

from app import app
from flask import render_template
from flask import request, session
import json
import copy
from ..db_operating import User, get_coll

from .computer import get_student, computer


@app.route('/find')
def find():
    return render_template('find.html')


@app.route('/list', methods=['POST'])
def ans():
    if request.method == 'POST':
        student = request.form['no']

        if student.isdigit():
            studentinfo = get_student(student)
            if studentinfo is not None:
                # 加入session
                session['user'] = studentinfo['gradelist']
                return render_template(
                    'ans.html',
                    info=studentinfo['gradelist'],
                    point=studentinfo['pointinfo']
                )

    return render_template('find.html')


@app.route('/update', methods=['POST'])
def update():
    if request.method == 'POST':
        # student = request.form['no']
        gradelist = copy.deepcopy(session['user'])
        len = 1
        for grade in gradelist['gradelist']:
            grade['grade'] = request.form['c' + str(len)]
            len += 1

        gradelist = computer(gradelist)
        return render_template(
            'ans.html',
            info=session['user'],
            point=gradelist
        )

    return render_template('find.html')


@app.route('/api', methods=['POST'])
def api():
    if request.method == 'POST':
        student = request.form['no']
        if student.isdigit():
            studentinfo = get_student(student)
            if studentinfo is not None:
                return json.dumps({
                    'point': studentinfo['pointinfo']['point'],
                })


@app.route('/wechat/jwc', methods=['GET', 'POST'])
def wechat_jwc():
    wechat_id = request.args.get('wechat_id')
    db = get_coll()
    a = db.users.find({"wechat_id": wechat_id}, {"wechat_id": 1, "_id": 0})
    student = ''
    for i in a:
        student = i['stu_id']
    if student.isdigit():
        studentinfo = get_student(student)
        if studentinfo is not None:
            # 加入session
            session['user'] = studentinfo['gradelist']
            return render_template(
                'ans.html',
                info=studentinfo['gradelist'],
                point=studentinfo['pointinfo']
            )
