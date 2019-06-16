from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
from wtforms.validators import Email

class LoginForm(FlaskForm):
    username = StringField("Käyttäjätunnus", [validators.required()])
    password = PasswordField("Salasana", [validators.required()])

    class Meta:
        csrf = False

class RegisterForm(FlaskForm):
    name = StringField("Nimi", [validators.required(), validators.Length(min=5, max=50)])
    username = StringField("Käyttäjätunnus", [validators.required(), validators.Length(min=3, max=50)])
    password = PasswordField("Salasana", [validators.required(), validators.Length(min=5, max=50)])
    email = StringField("Sähköpostiosoite", [validators.required(), validators.Email()])
    class Meta:
        csrf = False

class ModifyForm(FlaskForm):
    password = PasswordField("Uusi salasana", [validators.required(), validators.Length(min=5, max=50), validators.EqualTo("confirm", message="Salasanojen täytyy olla samat")])
    confirm = PasswordField("Toista salasana")

    class Meta:
        csrf = False