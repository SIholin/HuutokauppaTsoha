from application import db
from application.models import Base

from sqlalchemy.sql import text

class Image(Base):

    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)