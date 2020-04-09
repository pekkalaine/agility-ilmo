from flask_wtf import FlaskForm
from wtforms import StringField, validators, IntegerField, FormField

from wtforms_alchemy import ModelFieldList
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from application import db
from application.courses.models import Course


class CourseForm(FlaskForm):
    
    name = StringField("Kurssin nimi", [validators.InputRequired()])
    description = StringField("Kurssikuvaus", [validators.InputRequired()])
    max_participants = IntegerField("Osallistujamäärä", [validators.InputRequired()])

    class Meta:
        csrf = False

def get_courses():
    return Course.query


class CoursesForm(FlaskForm):
    course = QuerySelectField('Course', [validators.InputRequired(u'Valitse kurssi')],
                                query_factory=get_courses, get_label='name', allow_blank=True)

    class Meta:
        csrf = False
