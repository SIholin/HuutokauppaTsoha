from application import db
from application.models import Base

class Product(Base):
    
    name = db.Column(db.String(144), nullable=False)
    description = db.Column(db.String(500))
    onSale = db.Column(db.Boolean, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    offers = db.relationship("Offer", backref='product', lazy=True)
    tags = db.relationship("TagProduct", backref='product', lazy=True)

    def __init__(self, name, description):
        self.name = name
        self.description = description

  
        
    
    

   
