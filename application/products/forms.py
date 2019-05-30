from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, validators

class ProductForm(FlaskForm):
    name = StringField("Product name", [validators.required(), validators.Length(max=100)])
    description = TextAreaField("Description", [validators.optional(), validators.Length(max=500)])
    price = IntegerField("Price", [validators.required()])

    class Meta:
        csrf = False