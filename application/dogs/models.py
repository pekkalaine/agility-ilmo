from application import db
from application.models import Base

from sqlalchemy.sql import text


class Dog(Base):

    __tablename__ = "dog"
    
    race = db.Column(db.String(200), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False) 
                           
    enrolment = db.relationship("Enrolment", backref='dog', lazy=True)
    
    def __init__(self, name, race):
        self.name = name
        self.race = race

    @staticmethod
    def find_dogs_of_user(user_id):

        stmt = text("SELECT Dog.id, Dog.name, Dog.race FROM Dog"
                     " WHERE Dog.account_id  =  :user_id").params(user_id=user_id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1], "race":row[2]})

        return response

    @staticmethod
    def find_dogs_by_enrolment(course_id):
        stmt = text("SELECT Dog.id, Dog.name, Dog.race, dog.account_id FROM Dog"
                     " LEFT JOIN Enrolment ON Enrolment.dog_id = Dog.id"
                     " WHERE (Enrolment.course_id  =  :course_id)"
                     " GROUP BY Dog.id").params(course_id=course_id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1], "race":row[2], "account_id":row[3]})

        return response
