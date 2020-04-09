from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators


class LoginForm(FlaskForm):

    name = StringField("Nimi", [validators.InputRequired(), validators.Length(min=5, max=25, message="Nimessä on oltava 5-25 merkkiä")])
    username = StringField("Käyttäjätunnus", [validators.InputRequired(), validators.Length(min=3, max=10, message="Käyttäjätunnuksessa on oltava 3-10 merkkiä")])
    password = PasswordField("Salasana", [validators.InputRequired(), validators.Length(min=5, max=25, message="Salasanassa on oltava 5-25 merkkiä")])

    class Meta:
        csrf = False

