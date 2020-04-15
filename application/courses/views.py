from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application import app, db, login_required

from application.courses.models import Course
from application.courses.forms import CourseForm
from application.enrolments.models import Enrolment


@app.route("/courses", methods=["GET"])
@login_required(role="ADMIN")
def courses_index():
    return render_template("courses/list.html", courses=Course.query.all(), form=CourseForm())


@app.route("/courses/new/")
@login_required(role="ADMIN")
def courses_form():
    return render_template("courses/new.html", form=CourseForm())


@app.route("/courses/", methods=["POST"])
@login_required(role="ADMIN")
def courses_create():
    form = CourseForm(request.form)

    if not form.validate():
        return render_template("courses/new.html", form=form)

    c = Course(form.name.data, form.description.data, form.max_participants.data)

    db.session().add(c)
    db.session().commit()

    return redirect(url_for("courses_index"))


@app.route('/courses/delete/<int:id>')
@login_required(role="ADMIN")
def delete_course(id):
    course_to_delete = Course.query.get_or_404(id)

    #onko kurssille ilmoittautumisia:
    enrolments = Enrolment.find_enrolments_by_course(course_to_delete.id)

    if enrolments:
        return redirect(url_for("courses_index"))

    db.session.delete(course_to_delete)
    db.session.commit()

    return redirect(url_for("courses_index"))


@app.route('/courses/update/<int:id>', methods=["GET", "POST"])
@login_required(role="ADMIN")
def update_course(id):
    course = Course.query.get_or_404(id)

    if request.method == 'POST':

        form = CourseForm(request.form)

        if not form.validate():
            return render_template("/courses", form=form)

        course.name = form.name.data
        course.description = form.description.data
        course.max_participants = form.max_participants.data
       
        db.session.commit()

        return redirect('/courses')
    
    else:
        return render_template('courses/update.html', course=course, form=CourseForm())
        