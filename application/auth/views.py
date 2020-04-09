from application import app, db

from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required

from application.auth.models import User
from application.auth.forms import LoginForm
from application.dogs.forms import DogForm

from application.dogs.models import Dog

@app.route("/auth/login", methods=["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form=LoginForm())

    form = LoginForm(request.form)
    # mahdolliset validoinnit

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                               error = "Käyttäjätunnusta tai salasanaa ei löydy")

    login_user(user)
    return redirect(url_for("index"))

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/users/", methods=["GET"])
@login_required
def users_index():
    return render_template("users/list.html", users=User.query.all(), dogs=Dog.query.all(),  form=DogForm())

@app.route("/users/new/")
def users_form():
    return render_template("users/new.html", form=LoginForm())

@app.route("/users/", methods=["POST"])
def users_create():
    form = LoginForm(request.form)

    if not form.validate():
        return render_template("users/new.html", form=form)

    c = User(form.name.data, form.username.data, form.password.data)

    #Onko käyttäjä jo tietokannassa:
    user = User.query.filter_by(username=form.username.data).first()
    if user:
        return render_template("users/new.html", form=form, error="Käyttäjätunnus on jo olemassa.")


    db.session().add(c)
    db.session().commit()

    return redirect(url_for("auth_login"))


@app.route('/users/delete/<int:id>')
@login_required
def delete_user(id):
    user_to_delete = User.query.get_or_404(id)

    db.session.delete(user_to_delete)
    db.session.commit()

    return redirect(url_for("users_index"))


@app.route('/users/update/<int:id>', methods=["GET", "POST"])
@login_required
def update_user(id):
    user = User.query.get_or_404(id)


    if request.method == 'POST':
        form = LoginForm(request.form)

        if not form.validate():
            return render_template("/dogs", form=form)

        user.name = form.name.data
        user.username = form.username.data

        db.session.commit()
        return redirect('/users')

    else:
        return render_template('users/update.html', user=user, form = LoginForm())


@app.route("/users/byrace", methods=["POST"])
@login_required
def users_byrace():

    form = DogForm(request.form)
    race = form.race.data
    
    return render_template("/users/byrace.html", race_owners=User.find_users_with_race(race), race=race)
