from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.dogs.models import Dog
from application.courses.models import Course
from application.enrolments.models import Enrolment
from application.auth.models import User

from application.courses.forms import CoursesForm


@app.route("/enrolments", methods=["POST"])
@login_required
def new_enrolment():
    course_form = CoursesForm(request.form)
    course_id = course_form.course.data.id
    dog_id = request.form.get("dog_id")

    course_to_enrol = Course.query.get_or_404(course_id)
    dog_to_enrol = Dog.query.get_or_404(dog_id)

    return render_template("enrolments/new.html", course=course_to_enrol, dog=dog_to_enrol)


@app.route("/enrolments/add", methods=["POST"])
@login_required
def enrolment_add():
    course_id = request.form.get("course_id")
    dog_id = request.form.get("dog_id")

    course = Course.query.get_or_404(course_id)
    dog = Dog.query.get_or_404(dog_id)

    #onko jo ilmoittautunut:
    enrolment = Enrolment.query.filter_by(dog_id=dog_id, course_id=course_id).first()

    if enrolment:
        error = dog.name + ' on jo ilmoittautunut kurssille ' + course.name
        return render_template('/enrolments/exists.html', error=error)

    c = Enrolment(course_id, dog_id)
    db.session().add(c)
    db.session().commit()

    return redirect('/dogs')


@app.route("/enrolments/exists", methods=["GET"])
@login_required
def enrolment_exists():
    return redirect('/enrolments/exists')


@app.route("/enrolments/cancel", methods=["POST", "GET"])
@login_required
def enrolments_cancel():
    course_id = request.form.get("course_id")
    dog_id = request.form.get("dog_id")

    course = Course.query.get_or_404(course_id)

    enrolment_to_delete = Enrolment.query.filter_by(dog_id=dog_id, course_id=course_id).first()

    db.session.delete(enrolment_to_delete)
    db.session.commit()

    return render_template("/dogs/byenrolment.html", dogs=Dog.find_dogs_by_enrolment(course_id), course=course)

""" 
@app.route("/enrolments/cancel_bydog", methods=["POST", "GET"])
@login_required
def enrolments_cancel_bydog():

    user_id = current_user.id
    form = CoursesForm()
    user = User.query.get_or_404(user_id)
    dogs = Dog.find_dogs_of_user(user_id)

    courses = Course.query.all()
    enrolments = Enrolment.query.all()

    enrolment_id = request.form.get("enrolment_id")
    enrolment_to_delete = Enrolment.query.filter_by(id=enrolment_id).first()

    db.session.delete(enrolment_to_delete)
    db.session.commit()

    return redirect(url_for("dogs_index", dogs=dogs, user=user, courses=courses, enrolments=enrolments, form=form))
 """