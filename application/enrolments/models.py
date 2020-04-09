from application import db
from application.models import Base
from application.courses.models import Course
from application.dogs.models import Dog

from sqlalchemy.sql import text


class Enrolment(db.Model):

    __tablename__ = "enrolment"

    id = db.Column(db.Integer, primary_key=True)   
    course_id = db.Column(db.ForeignKey(Course.id),
                           nullable=False)
    dog_id = db.Column(db.ForeignKey(Dog.id),
                           nullable=False)

