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

    nro_of_dogs = len(dogs)

    courses = Course.query.all()
    
    return render_template("dogs/list.html", dogs=dogs, user=user, courses=courses, 
                nro_of_dogs=nro_of_dogs, form=form)

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
        error = "Poista ensin koiran " +  dog_to_delete.name + " kurssi-ilmoittautumiset"
        return render_template('/dogs/error.html', error=error)

    if (dog_to_delete.account_id != current_user.id):
        error = "Voit poistaa vain omia koiriasi."
        return render_template('/dogs/error.html', error=error)

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

            print('******************* tadaa')
            return render_template('dogs/update.html', dog=dog, 
                form=DogForm(name=dog.name, race=dog.race))

        dog.name = form.name.data
        dog.race = form.race.data
       
        db.session.commit()
        return redirect('/dogs/')
    
    else:

        if (dog.account_id != current_user.id):
            error = "Voit päivittää vain omien koiriesi tietoja."
            return render_template('/dogs/error.html', error=error)

        return render_template('dogs/update.html', dog=dog, 
                form=DogForm(name=dog.name, race=dog.race))


@app.route("/dogs/byenrolment", methods=["POST"])
@login_required
def dogs_byenrolment():

    course_id = request.form.get("course_id")
    course = Course.query.get_or_404(course_id)
    dogs = Dog.find_dogs_by_enrolment(course_id)

    nr_of_dogs_on_course = len(dogs)

    return render_template("/dogs/byenrolment.html", dogs=dogs, course=course, nr_of_dogs_on_course=nr_of_dogs_on_course)
