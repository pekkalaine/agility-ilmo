from flask_wtf import FlaskForm
from wtforms import StringField, validators, IntegerField


class DogForm(FlaskForm):
    id = IntegerField("Kurssin id", [validators.InputRequired()])
    name = StringField("Koiran nimi", [validators.InputRequired()])
    race = StringField("Koiran rotu", [validators.InputRequired()])

    class Meta:
        csrf = False
