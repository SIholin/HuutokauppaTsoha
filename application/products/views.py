from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.products.models import Product
from application.products.forms import ProductForm
from application.offer.models import Offer

@app.route("/products", methods=["GET"])
def products_index():
   
    return render_template("products/list.html", products = Product.query.all(), offers = Offer.query.all())

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

@app.route("/products/change/price/<product_id>/", methods=["POST"])
@login_required
def products_set_new_price(product_id):
    p = Product.query.get(product_id)
    p.price = request.form.get("new_price")
    db.session().commit()

    return redirect(url_for("products_index"))

@app.route("/products/delete/<product_id>/", methods=["POST"])
@login_required
def products_delete(product_id):
    p = Product.query.get(product_id)
    db.session.delete(p)
    db.session.commit()

    return redirect(url_for("products_index"))

@app.route("/products/offer/<product_id>", methods=["POST"])
@login_required
def products_offer(product_id):
    
    o = Offer(request.form.get("offer"))
    
    o.account_id = current_user.id
    o.product_id = product_id
    db.session().add(o)
    db.session().commit()

    return redirect(url_for("products_index"))