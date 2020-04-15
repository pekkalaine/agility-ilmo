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


    def __init__(self, course_id, dog_id):
            self.course_id = course_id
            self.dog_id = dog_id


    @staticmethod
    def find_enrolments_by_dog(dog_id):

        stmt = text("SELECT * FROM Enrolment"
                     " WHERE Enrolment.dog_id  =  :dog_id").params(dog_id=dog_id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1], "race":row[2]})

        return response

    @staticmethod
    def find_enrolments_by_course(course_id):

        stmt = text("SELECT * FROM Enrolment"
                     " WHERE Enrolment.course_id  =  :course_id").params(course_id=course_id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1], "race":row[2]})

        return response