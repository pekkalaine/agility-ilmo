from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required

from application.auth.models import User
from application.dogs.models import Dog
from application.users.forms import UserForm

@app.route("/users/", methods=["GET"])
def users_index():
    return render_template("users/list.html", users=User.query.all(), dogs=Dog.query.all())


@app.route("/users/new/")
def users_form():
    return render_template("users/new.html", form=UserForm())


@app.route("/users/", methods=["POST"])
def users_create():
    form = UserForm(request.form)

    if not form.validate():
        return render_template("users/new.html", form=form)

    c = User(form.name.data, form.username.data, form.password.data)

    db.session().add(c)
    db.session().commit()

    return redirect(url_for("users_index"))


@app.route('/users/delete/<int:id>')
def delete_user(id):
    user_to_delete = User.query.get_or_404(id)

    db.session.delete(user_to_delete)
    db.session.commit()

    return redirect(url_for("users_index"))


@app.route('/users/update/<int:id>', methods=["GET", "POST"])
def update_user(id):
    user = User.query.get_or_404(id)

    if request.method == 'POST':

        user.name = request.form['user_name']
        user.race = request.form['user_username']

        db.session.commit()
        return redirect('/users')

    else:
        return render_template('users/update.html', user=user)
