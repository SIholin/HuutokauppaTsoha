from application import db
from application.models import Base
from application.tag.models import Tag
from application.products.models import Product

from sqlalchemy.sql import text

class TagProduct(Base):

    product_id = db.Column(db.Integer, db.ForeignKey("product.id"), nullable=False)
    tag_id = db.Column(db.Integer, db.ForeignKey("tag.id"), nullable=False)

    def __init__(self, product_id, tag_id):
        self.product_id = product_id
        self.tag_id = tag_id

    @staticmethod
    def tags_by_product_id(product_id):
        
        tps = TagProduct.query.filter(TagProduct.product_id == product_id)
        tags = []
        for t in tps:
            tags.append(Tag.query.get(t.tag_id))

        return tags

    @staticmethod
    def products_by_tag_id(tag_id):
        
        tps = TagProduct.query.filter(TagProduct.tag_id == tag_id)
        products = []
        for tp in tps:
            products.append(Product.query.get(tp.product_id))

        return products
