from application import db
from application.models import Base

from sqlalchemy.sql import text

class User(Base):

    __tablename__ = "account"

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(144), nullable=False)

    offers = db.relationship("Offer", backref='account', lazy=True)
    products = db.relationship("Product", backref='account', lazy=True)

    def __init__(self, name, username, password, email):
        self.name = name
        self.username = username
        self.password = password
        self.email = email

    def get_id(self):
        return self.id
    
    def is_active(self):
        return True

    def is_anonymous(self):
        return False
    
    def is_authenticated(self):
        return True
    
    def roles(self):
        return [self.role]
    
    def is_admin(self):
        return self.role == "ADMIN"

    @staticmethod
    def find_how_many_products():
        stmt = text("SELECT Account.id, Account.name, COUNT(Product.id) FROM Account"
                    " LEFT JOIN Product ON Product.account_id = Account.id"
                    " GROUP BY Account.id")
        
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1], "amount":row[2]})

        return response


    @staticmethod
    def find_price_max():
        stmt = text("SELECT Account.id, Account.name, Max(Offer.price) FROM Account"
                    " LEFT JOIN Offer ON Offer.account_id = Account.id"
                    " GROUP BY Account.id")
        
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1], "value":row[2]})

        return response

    @staticmethod
    def find_offer_average():
        stmt = text("SELECT Account.id, Account.name, AVG(Offer.price) FROM Account"
                    " LEFT JOIN Offer ON Offer.account_id = Account.id"
                    " GROUP BY Account.id")
        
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1], "average":row[2]})

        return response

    @staticmethod
    def find_offer_min():
        stmt = text("SELECT Account.id, Account.name, Min(Offer.price) FROM Account"
                    " LEFT JOIN Offer ON Offer.account_id = Account.id"
                    " GROUP BY Account.id")
        
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1], "value":row[2]})

        return response