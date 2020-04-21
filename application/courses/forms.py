from flask_wtf import FlaskForm
from wtforms import StringField, validators, IntegerField, FormField

from wtforms_alchemy import ModelFieldList
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from application import db
from application.courses.models import Course


class CourseForm(FlaskForm):
    
    name = StringField("Kurssin nimi", [validators.InputRequired(), validators.length(max=15, message="Nimessä voi olla enintään 15 merkkiä.")])
    description = StringField("Kurssikuvaus", [validators.InputRequired(), validators.length(max=200, message="Kuvauksessa voi olla enintään 15 merkkiä.")])
    max_participants = IntegerField("Osallistujamäärä", [validators.InputRequired(), validators.NumberRange(min=1, max=20, message="Kurssilla voi olla enintään 20 koiraa.")])

    class Meta:
        csrf = False

def get_courses():
    return Course.query


class CoursesForm(FlaskForm):
    course = QuerySelectField('Course', [validators.InputRequired(u'Valitse kurssi')],
                                query_factory=get_courses, get_label='name', allow_blank=False)

    class Meta:
        csrf = False
