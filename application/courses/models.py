from application import db
from application.models import Base


class Course(Base):

    __tablename__ = "course"
    
    description = db.Column(db.String(400), nullable=False)
    max_participants = db.Column(db.Integer, nullable=False)

    enrolment = db.relationship("Enrolment", backref='course', lazy=True)

    def __init__(self, name, description, max_participants):
        self.name = name
        self.description = description
        self.max_participants = max_participants
