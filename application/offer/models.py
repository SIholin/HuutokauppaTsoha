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
        return Offer.query.filter(Offer.product_id == product_id)

