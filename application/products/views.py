from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.products.models import Product
from application.products.forms import ProductForm
from application.offer.models import Offer
from application.auth.models import User

@app.route("/products", methods=["GET"])
def products_index():
   
    return render_template("products/list.html", products = Product.query.all(), get_account = User.query.get)

@app.route("/products/new/")
@login_required
def products_form():
    return render_template("products/new.html", form = ProductForm())

@app.route("/products/", methods=["POST"])
@login_required
def products_create():
    form = ProductForm(request.form)

    if not form.validate():
        return render_template("products/new.html", form = form)
    
    p = Product(form.name.data, form.description.data, form.price.data)
    p.account_id = current_user.id

    db.session().add(p)
    db.session().commit()

    return redirect(url_for("products_index"))

@app.route("/products/<product_id>/", methods=["GET"])
def product_index(product_id):
    p = Product.query.get(product_id)
    owner = User.query.get(p.account_id)
    return render_template("products/product.html", product = p, get_account = User.query.get, get_offers = Offer.by_product, owner = owner)

@app.route("/products/change/description/<product_id>/", methods=["POST"])
@login_required
def products_set_new_description(product_id):
    p = Product.query.get(product_id)

    if current_user.id == p.account_id:
        p.description = request.form.get("new_description")
        db.session().commit()

    return redirect(url_for("product_index", product_id = product_id))

@app.route("/products/delete/<product_id>/", methods=["POST"])
@login_required
def products_delete(product_id):
    p = Product.query.get(product_id)

    if current_user.id == p.account_id:
        db.session.delete(p)
        db.session.commit()

    return redirect(url_for("product_index", product_id = product_id))

@app.route("/products/offer/<product_id>", methods=["POST"])
@login_required
def products_offer(product_id):
    amount = request.form.get("offer")
    p = Product.query.get(product_id)

    if current_user.id != p.account_id:
    
        if  int(amount) <= p.price:
            return render_template("products/product.html", e = 1, product = p, get_account = User.query.get, get_offers = Offer.by_product)
    
        o = Offer(amount)
        o.account_id = current_user.id
        o.product_id = product_id
        p.price = amount
        db.session().add(o)
        db.session().add(p)
        db.session().commit()

    return redirect(url_for("product_index", product_id = product_id))