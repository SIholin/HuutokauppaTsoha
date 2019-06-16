from application import db
from application.models import Base

class Tag(Base):

    name = db.Column(db.String(144), nullable=False)

    products = db.relationship("TagProduct", backref='tag', lazy=True)

    def __init__(self, name):
        self.name = name
