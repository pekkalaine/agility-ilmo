from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.dogs.models import Dog
from application.auth.models import User
from application.dogs.forms import DogForm


@app.route("/dogs", methods=["GET"])
@login_required
def dogs_index():
    return render_template("dogs/list.html", dogs=Dog.query.all(), users=User.query.all())


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

    db.session.delete(dog_to_delete)
    db.session.commit()

    return redirect(url_for("dogs_index"))


@app.route('/update/<int:id>', methods=["GET", "POST"])
@login_required
def update(id):
    dog = Dog.query.get_or_404(id)

    if request.method == 'POST':

        dog.name = request.form['dog_name']
        dog.race = request.form['dog_race']

        db.session.commit()
        return redirect('/dogs')
    
    else:
        return render_template('dogs/update.html', dog=dog)