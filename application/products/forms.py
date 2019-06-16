from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators

class ProductForm(FlaskForm):
    name = StringField("Nimi", [validators.required(), validators.Length(max=100)])
    description = TextAreaField("Kuvaus", [validators.optional(), validators.Length(max=500)])

    class Meta:
        csrf = False
