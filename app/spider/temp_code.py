'''
            if stu_id == "13":
                form_1 = AfterJwcFor2013_2014_1()
                form_2 = AfterJwcFor2013_2014_1()
                form_3 = AfterJwcFor2014_2015_1()
                form_4 = AfterJwcFor2014_2015_2()
                form_5 = AfterJwcFor2015_2016_1()
                form_6 = AfterJwcFor2015_2016_1()
                if form_1.validate_on_submit():
                    return_data = post_for_score("2013-2014", "1")
                    return render_template("jwc_score.html", return_data=return_data, stu_base_info=stu_base_info, class_info=class_info)
                elif form_2.is_submitted():
                    return_data = post_for_score("2013-2014", "2")
                    return render_template("jwc_score.html", return_data=return_data, stu_base_info=stu_base_info, class_info=class_info)
                elif form_3.is_submitted():
                    return_data = post_for_score("2014-2015", "1")
                    return render_template("jwc_score.html", return_data=return_data,stu_base_info=stu_base_info, class_info=class_info)
                elif form_4.is_submitted():
                    return_data = post_for_score("2014-2015", "2")
                    return render_template("jwc_score.html", return_data=return_data,stu_base_info=stu_base_info, class_info=class_info)
                elif form_5.is_submitted():
                    return_data = post_for_score("2015-2016", "1")
                    return render_template("jwc_score.html", return_data=return_data,stu_base_info=stu_base_info, class_info=class_info)
                elif form_6.is_submitted():
                    return_data = post_for_score("2015-2016", "2")
                    return render_template("jwc_score.html", return_data=return_data,stu_base_info=stu_base_info, class_info=class_info)

                return render_template('jwc.html', stu_base_info=stu_base_info, class_info=class_info)
            elif stu_id == "14":
                stu_base_info1 = stu_base_info
                form_1 = AfterJwcFor2013_2014_1()
                form_2 = AfterJwcFor2013_2014_1()
                form_3 = AfterJwcFor2014_2015_1()
                form_4 = AfterJwcFor2014_2015_2()
                if form_1.validate_on_submit():
                    return_data = post_for_score("2013-2014", "1")
                    return render_template("jwc_score.html", return_data=return_data)
                elif form_2.is_submitted():
                    return_data = post_for_score("2013-2014", "1")
                    return render_template("jwc_score.html", return_data=return_data)
                elif form_3.is_submitted():
                    return_data = post_for_score("2014-2015", "1")
                    return render_template("jwc_score.html", return_data=return_data)
                elif form_4.is_submitted():
                    return_data = post_for_score("2014-2015", "2")
                    return render_template("jwc_score.html", return_data=return_data)

                return "%r"%stu_base_info1
            elif stu_id == "15":
                form_1 = AfterJwcFor2013_2014_1()
                form_2 = AfterJwcFor2013_2014_1()
                if form_1.validate_on_submit():
                    return_data = post_for_score("2013-2014", "1")
                    return render_template("jwc_score.html", return_data=return_data)
                elif form_2.is_submitted():
                    return_data = post_for_score("2013-2014", "1")
                    return render_template("jwc_score.html", return_data=return_data)
                return render_template('jwc.html', stu_base_info=stu_base_info, class_info=class_info)
'''''