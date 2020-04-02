from flask_wtf import FlaskForm
from wtforms import StringField, validators, IntegerField


class CourseForm(FlaskForm):
    name = StringField("Kurssin nimi", [validators.InputRequired()])
    description = StringField("Kurssikuvaus", [validators.InputRequired()])
    max_participants = IntegerField("Osallistujamäärä", [validators.InputRequired()])

    class Meta:
        csrf = False
