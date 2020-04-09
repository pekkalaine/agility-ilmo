from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db

from application.courses.models import Course

from application.courses.forms import CourseForm


@app.route("/courses", methods=["GET"])
def courses_index():
    return render_template("courses/list.html", courses=Course.query.all())


@app.route("/courses/new/")
@login_required
def courses_form():
    return render_template("courses/new.html", form=CourseForm())


@app.route("/courses/", methods=["POST"])
@login_required
def courses_create():
    form = CourseForm(request.form)

    if not form.validate():
        return render_template("courses/new.html", form=form)

    c = Course(form.name.data, form.description.data, form.max_participants.data)

    db.session().add(c)
    db.session().commit()

    return redirect(url_for("courses_index"))


@app.route('/courses/delete/<int:id>')
@login_required
def delete_course(id):
    course_to_delete = Course.query.get_or_404(id)

    db.session.delete(course_to_delete)
    db.session.commit()

    return redirect(url_for("courses_index"))


@app.route('/courses/update/<int:id>', methods=["GET", "POST"])
@login_required
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
        