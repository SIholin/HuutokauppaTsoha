from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators

class LoginForm(FlaskForm):
    username = StringField("Käyttäjätunnus", [validators.required()])
    password = PasswordField("Salasana", [validators.required()])

    class Meta:
        csrf = False

class RegisterForm(FlaskForm):
    name = StringField("Nimi", [validators.required(), validators.Length(min=5, max=50)])
    username = StringField("Käyttäjätunnus", [validators.required(), validators.Length(min=3, max=50)])
    password = PasswordField("Salasana", [validators.required(), validators.Length(min=5, max=50)])

    class Meta:
        csrf = False