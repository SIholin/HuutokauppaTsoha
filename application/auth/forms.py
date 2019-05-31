from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators

class LoginForm(FlaskForm):
    username = StringField("Username", [validators.required()])
    password = PasswordField("Password", [validators.required()])

    class Meta:
        csrf = False

class RegisterForm(FlaskForm):
    name = StringField("Name", [validators.required(), validators.Length(min=5, max=50)])
    username = StringField("Username", [validators.required(), validators.Length(min=3, max=50)])
    password = PasswordField("Password", [validators.required(), validators.Length(min=5, max=50)])

    class Meta:
        csrf = False