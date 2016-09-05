from app.main import main
from app import db
from app.models import Message
from flask import render_template, request, redirect, url_for, flash
from datetime import datetime


@main.route('/part-time-job')
def part_time_job():
    return render_template(
        'main/part_time_job.html',
        title=u'兼职平台',
        year=datetime.now().year,
    )


@main.route('/part-time-job/manage', methods=['GET', 'POST'])
def part_time_job_manage():
    if request.method == 'GET':
        return render_template(
            'main/part_time_job_manage.html',
            title=u'兼职平台信息管理',
            job_time=datetime.now(),
            year=datetime.now().year,
        )
    else:
        job_time = request.form['job_time']
        job_title = request.form['job_title']
        job_content = request.form['job_content']
        job_contact = request.form['job_contact']
        a_message = Message(title=job_title, date=job_time, content=job_content, contact=job_contact)
        db.session.add(a_message)
        db.session.commit()
        flash(u"兼职信息已经发布")
        return redirect(url_for("main.part_time_job_manage"))
