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
        error = "Poista ensin kaikki kurssin " +  course_to_delete.name + " ilmoittautumiset."
        return render_template('/courses/error.html', error=error)


    db.session.delete(course_to_delete)
    db.session.commit()

    return redirect(url_for("courses_index"))


@app.route('/courses/update/<int:id>', methods=["GET", "POST"])
@login_required(role="ADMIN")
def update_course(id):
    course = Course.query.get_or_404(id)

    enrolments = Enrolment.find_enrolments_by_course(id)
    nr_of_enrolments_on_course = len(enrolments)

    if request.method == 'POST':

        form = CourseForm(request.form)

        if not form.validate():
            return render_template('courses/update.html', course=course, 
                form=CourseForm(name=course.name, description=course.description, 
                max_participants=course.max_participants ))

        #updatessa määriteltävä max osallistujamäärä < jo ilmoittautuneet:

        if (form.max_participants.data < nr_of_enrolments_on_course):
            error = 'Kurssille ' + course.name + ' on ilmoittautunut jo ' + str(nr_of_enrolments_on_course) + ' koiraa. Et voi päivittää osallistujamäärää pienemmäksi kuin ' + str(nr_of_enrolments_on_course) + '.'
            return render_template('/courses/update_error.html', error=error)

        course.name = form.name.data
        course.description = form.description.data
        course.max_participants = form.max_participants.data

        db.session.commit()

        return redirect('/courses')
    
    else:
        return render_template('courses/update.html', course=course, 
                form=CourseForm(name=course.name, description=course.description, 
                max_participants=course.max_participants ))
