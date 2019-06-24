from flask_wtf import FlaskForm
from wtforms import StringField, validators

class TagForm(FlaskForm):
    name = StringField("Nimi", [validators.required(), validators.Length(max=100)])

    class Meta:
        csrf = False