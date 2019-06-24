from application import db
from application.models import Base
from application.tag.models import Tag

from sqlalchemy.sql import text

class TagProduct(Base):

    product_id = db.Column(db.Integer, db.ForeignKey("product.id"), nullable=False)
    tag_id = db.Column(db.Integer, db.ForeignKey("tag.id"), nullable=False)

    def __init__(self, user_id, tag_id):
        self.user_id = user_id
        self.tag_id = tag_id

    @staticmethod
    def tags_by_product_id(product_id):
        
        tps = TagProduct.query.filter(TagProduct.product_id == product_id)
        tags = []
        for t in tps:
            tags.append(Tag.query.get(t.tag_id))

        return tags
