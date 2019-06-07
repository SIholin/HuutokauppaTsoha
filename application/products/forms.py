from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, validators

class ProductForm(FlaskForm):
    name = StringField("Nimi", [validators.required(), validators.Length(max=100)])
    description = TextAreaField("Kuvaus", [validators.optional(), validators.Length(max=500)])
    price = IntegerField("Hinta", [validators.required()])

    class Meta:
        csrf = False

