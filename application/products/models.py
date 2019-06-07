from application import db
from application.models import Base

class Product(Base):
    
    name = db.Column(db.String(144), nullable=False)
    description = db.Column(db.String(500))
    price = db.Column(db.Integer, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    
    

   
