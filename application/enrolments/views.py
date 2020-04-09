from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.dogs.models import Dog
from application.auth.models import User
from application.dogs.forms import DogForm

from application.courses.forms import CoursesForm


@app.route("/enrolments", methods=["POST"])
@login_required

def new_enrolment():
    course_form = CoursesForm(request.form)
    course_id = course_form.course.data.id

    dog_id = request.form.get("dog_id")

    print('********************* course_id', course_id)
    print('********************* dog_id', dog_id)

    return redirect(url_for("dogs_index"))
