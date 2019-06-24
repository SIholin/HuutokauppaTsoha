from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user

from application import app, db, login_required
from application.auth.models import User
from application.offer.models import Offer
from application.products.models import Product
from application.auth.forms import LoginForm, RegisterForm, ModifyForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())
    
    form = LoginForm(request.form)

    if not form.validate():
        return render_template("auth/loginform.html", form = form)

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form, error = "Ei löydy käyttäjänimeä tai salasanaa")
    
    login_user(user)
    return redirect(url_for("index"))

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/auth/register", methods = ["GET", "POST"])
def auth_register():
    if request.method == "GET":
        return render_template("auth/registerform.html", form = RegisterForm())

    form = RegisterForm(request.form)

    if not form.validate():
        return render_template("auth/registerform.html", form = form)

    if  User.query.filter(User.username == form.username.data).first():
        return render_template("auth/registerform.html", form = RegisterForm(), error = "Käyttäjänimi jo käytössä")
    u = User(form.name.data, form.username.data, form.password.data, form.email.data)
    
    db.session().add(u)
    db.session().commit()

    return redirect(url_for("index"))

@app.route("/auth/profile/<account_id>/", methods=["GET", "POST"])
def auth_profile(account_id):
    u = User.query.get(account_id)
    products = Product.query.filter(account_id == account_id)
    if request.method == "GET":
        return render_template("auth/profile.html", get_account = User.query.get, products = products, account = u, form = ModifyForm())
   
    if current_user.id != u.id:
        return render_template("auth/profile.html", form = ModifyForm(), error = "Väärä käyttäjä")
    
    form = ModifyForm(request.form)

    if not form.validate():
        return render_template("auth/profile.html", form = form)

    u.password = form.password.data
    
    db.session().commit()

    return render_template(url_for("auth/profile.html",))

@app.route("/auth/delete/<account_id>/", methods=["POST"])
def auth_delete(account_id):
    u = User.query.get(account_id)
    offers = Offer.query.filter(Offer.account_id == account_id)
    for offer in offers:
        db.session().delete(offer)
        db.session().commit()
    if current_user.id == u.id:
        db.session().delete(u)
        db.session().commit()

    return redirect(url_for("index"))




