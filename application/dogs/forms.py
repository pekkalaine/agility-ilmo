from flask_wtf import FlaskForm
from wtforms import StringField, validators, IntegerField


class DogForm(FlaskForm):
    
    name = StringField("Koiran nimi", [validators.InputRequired()])
    race = StringField("Koiran rotu", [validators.InputRequired()])

    class Meta:
        csrf = False
