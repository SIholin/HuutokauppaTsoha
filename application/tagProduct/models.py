from application import db
from application.models import Base

class TagProduct(Base):

    product_id = db.Column(db.Integer, db.ForeignKey("product.id"), nullable=False)
    tag_id = db.Column(db.Integer, db.ForeignKey("tag.id"), nullable=False)

    def __init__(self, user_id, tag_id):
        self.user_id = user_id
        self.tag_id = tag_id

