from application import app, db
from flask import redirect, render_template, request, url_for
from application.dogs.models import Dog

from application.dogs.forms import DogForm

@app.route("/dogs", methods=["GET"])
def dogs_index():
    return render_template("dogs/list.html", dogs=Dog.query.all())


@app.route("/dogs/new/")
def dogs_form():
    return render_template("dogs/new.html", form=DogForm())


@app.route("/dogs/", methods=["POST"])
def dogs_create():
    form = DogForm(request.form)

    if not form.validate():
        return render_template("dogs/new.html", form=form)

    c = Dog(form.name.data, form.race.data)

    db.session().add(c)
    db.session().commit()

    return redirect(url_for("dogs_index"))


@app.route('/delete/<int:id>')
def delete(id):
    dog_to_delete = Dog.query.get_or_404(id)

    db.session.delete(dog_to_delete)
    db.session.commit()

    return redirect(url_for("dogs_index"))


@app.route('/update/<int:id>', methods=["GET", "POST"])
def update(id):
    dog = Dog.query.get_or_404(id)

    if request.method == 'POST':

        dog.name = request.form['dog_name']
        dog.race = request.form['dog_race']

        db.session.commit()
        return redirect('/dogs')
    
    else:
        return render_template('dogs/update.html', dog=dog)