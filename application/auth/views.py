from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user

from application import app, db, login_required
from application.auth.models import User
from application.offer.models import Offer
from application.products.models import Product
from application.auth.forms import LoginForm, RegisterForm, ModifyForm

#Mahdollistaa käyttäjän sisäänkirjautumisen
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

#Mahdollistaa käyttäjän uloskirjautumisen
@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))

#Uuden käyttäjän luonti
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
    u.role = "REGULAR"
    db.session().add(u)
    db.session().commit()
    login_user(u)

    return redirect(url_for("index"))

#Näyttää käyttäjän profiilin ja vaihtaa salasanan
@app.route("/auth/profile/<account_id>/", methods=["GET", "POST"])
def auth_profile(account_id):
    u = User.query.get(account_id)
    products = Product.query.filter(Product.account_id == account_id)

    if request.method == "GET":
        return render_template("auth/profile.html", get_account = User.query.get, products = products, account = u, form = ModifyForm())
    
    form = ModifyForm(request.form)

    if not form.validate():
        return render_template("auth/profile.html", get_account = User.query.get, products = products, account = u, form = form)

    u.password = form.password.data
    
    db.session().commit()

    return render_template("auth/profile.html", e = 1, get_account = User.query.get, products = products, account = u, form = form)

#Listaa käyttäjät
@app.route("/auth/list/", methods=["GET"])
@login_required(role="ADMIN")
def auth_index():
    return render_template("/auth/list.html", is_admin = User.is_admin, accounts = User.query.all())

#Tekee käyttäjästä ADMIN
@app.route("/auth/make/admin/<account_id>/", methods=["POST"])
@login_required(role="ADMIN")
def auth_make_admin(account_id):
    u = User.query.get(account_id)
    u.role = "ADMIN"
    db.session().commit()
    return redirect(url_for("auth_index"))

#Poistaa käyttäjän
@app.route("/auth/delete/<account_id>/", methods=["POST"])
def auth_delete(account_id):
    if current_user.id == account_id or current_user.is_admin:
        u = User.query.get(account_id)
        offers = Offer.query.filter(Offer.account_id == account_id)
        for offer in offers:
            db.session().delete(offer)
            db.session().commit()
        if current_user.id == u.id:
            db.session().delete(u)
            db.session().commit()

    return redirect(url_for("index"))




