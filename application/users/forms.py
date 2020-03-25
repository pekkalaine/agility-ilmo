from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators


class UserForm(FlaskForm):

    name = StringField("Nimi", [validators.InputRequired()])
    username = StringField("Käyttäjätunnus", [validators.InputRequired()])
    password = PasswordField("Salasana", [validators.InputRequired()])

    class Meta:
        csrf = False
