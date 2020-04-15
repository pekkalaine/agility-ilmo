from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.dogs.models import Dog
from application.auth.models import User
from application.courses.models import Course
from application.dogs.forms import DogForm

from application.enrolments.models import Enrolment

from application.courses.forms import CoursesForm

@app.route("/dogs/", methods=["GET"])
@login_required
def dogs_index():
    user_id = current_user.id
    form = CoursesForm()
    user = User.query.get_or_404(user_id)
    dogs = Dog.find_dogs_of_user(user_id)

    courses = Course.query.all()
    enrolments = Enrolment.query.all()
    
    return render_template("dogs/list.html", dogs=dogs, user=user, courses=courses, enrolments=enrolments, form=form)

@app.route("/dogs/new/")
@login_required
def dogs_form():
    return render_template("dogs/new.html", form=DogForm())


@app.route("/dogs/", methods=["POST"])
@login_required
def dogs_create():
    form = DogForm(request.form)

    if not form.validate():
        return render_template("dogs/new.html", form=form)

    c = Dog(form.name.data, form.race.data)
    c.account_id = current_user.id

    db.session().add(c)
    db.session().commit()

    return redirect(url_for("dogs_index"))


@app.route('/delete/<int:id>')
@login_required
def delete(id):
    dog_to_delete = Dog.query.get_or_404(id)

    enrolment = Enrolment.find_enrolments_by_dog(dog_to_delete.id)

    if enrolment:
        error = "Poista ensin koiran" +  dog_to_delete.name + "kurssi-ilmoittautumiset"

        return redirect(url_for("dogs_index"))

    db.session.delete(dog_to_delete)
    db.session.commit()

    return redirect(url_for("dogs_index"))


@app.route('/update/<int:id>', methods=["GET", "POST"])
@login_required
def update(id):
    dog = Dog.query.get_or_404(id)

    if request.method == 'POST':

        form = DogForm(request.form)

        if not form.validate():
            return render_template("/dogs/", form=form)

        dog.name = form.name.data
        dog.race = form.race.data
       
        db.session.commit()
        return redirect('/dogs/')
    
    else:
        return render_template('dogs/update.html', dog=dog, form=DogForm())

@app.route("/dogs/byenrolment", methods=["POST"])
@login_required
def dogs_byenrolment():

    course_id = request.form.get("course_id")
    course = Course.query.get_or_404(course_id)

    return render_template("/dogs/byenrolment.html", dogs=Dog.find_dogs_by_enrolment(course_id), course=course)