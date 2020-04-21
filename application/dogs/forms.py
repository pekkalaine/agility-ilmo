from flask_wtf import FlaskForm
from wtforms import StringField, validators, IntegerField


class DogForm(FlaskForm):
    
    name = StringField("Koiran nimi", [validators.InputRequired(), validators.Length(min=2, max=25, message="Nimessä on oltava 2-25 merkkiä")])
    race = StringField("Koiran rotu", [validators.InputRequired(), validators.Length(min=2, max=25, message="Rodussa on oltava 2-25 merkkiä")])

    class Meta:
        csrf = False
