from application import db
from application.models import Base

from sqlalchemy.sql import text

class Offer(Base):

    price = db.Column(db.Integer, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)

    def __init__(self, price):
        self.price = price

    def by_product(product_id):
        offers = Offer.query.filter(Offer.product_id == product_id)
        return offers.order_by(Offer.price.desc())

    @staticmethod
    def get_biggest_offer(product_id):
        stmt = text("SELECT MAX(price) FROM offer "
                    "WHERE offer.product_id = :id").params(id = product_id)
        res = db.engine.execute(stmt)
        
        for row in res:
           return row[0]
        
        
