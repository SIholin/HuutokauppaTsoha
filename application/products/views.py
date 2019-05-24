from application import app, db
from flask import redirect, render_template, request, url_for
from application.products.models import Product

@app.route("/products", methods=["GET"])
def products_index():
    return render_template("products/list.html", products = Product.query.all())

@app.route("/products/new/")
def products_form():
    return render_template("products/new.html")

@app.route("/products/", methods=["POST"])
def products_create():
    p = Product(request.form.get("name"), request.form.get("description"), request.form.get("price"))

    db.session().add(p)
    db.session().commit()

    return redirect(url_for("products_index"))

@app.route("/products/<product_id>/", methods=["POST"])
def products_set_new_price(product_id):
    p = Product.query.get(product_id)
    p.price = request.form.get("new_price")
    db.session().commit()

    return redirect(url_for("products_index"))