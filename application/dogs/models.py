from application import db
from application.models import Base


class Dog(Base):
    
    race = db.Column(db.String(200), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    def __init__(self, name, race):
        self.name = name
        self.race = race
