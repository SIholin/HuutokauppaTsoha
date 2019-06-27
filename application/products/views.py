from flask import redirect, render_template, request, url_for
from flask_login import current_user
from sqlalchemy import func

from application import app, db, login_required
from application.products.models import Product
from application.products.forms import ProductForm
from application.offer.models import Offer
from application.auth.models import User
from application.tag.models import Tag
from application.tagProduct.models import TagProduct

#Listaa tuotteet ja mahdollisuus lisätä uusi tuote
@app.route("/products/", methods=["GET"])
def products_index():
    return render_template("products/list.html", form = ProductForm(), biggest_offer = Offer.get_biggest_offer, products = Product.query.all(), get_account = User.query.get)

#Käsittelee uuden lisätyn tuotteen
@app.route("/products/", methods=["POST"])
@login_required()
def products_create():
    form = ProductForm(request.form)

    if not form.validate():
        return render_template("products/new.html", form = form)
    
    p = Product(form.name.data, form.description.data)
    p.account_id = current_user.id
    p.onSale = True

    db.session().add(p)
    db.session().commit()

    return redirect(url_for("products_index"))

#Hakee tuotteita hakusanan perusteella
@app.route("/products/search/", methods=["POST"])
def products_search():

    search = request.form.get("name")

    if not search:
        products = Product.query.all()
    else:
        products = Product.query.filter(Product.name.contains(search))

    return render_template("products/list.html", biggest_offer = Offer.get_biggest_offer, get_account = User.query.get, products = products)

#Näyttää yhden tuotteen
@app.route("/product/<product_id>/", methods=["GET"])
def product_index(product_id):
    p = Product.query.get(product_id)
    owner = User.query.get(p.account_id)
    tags = TagProduct.tags_by_product_id(product_id)
    biggest_offer = Offer.get_biggest_offer(product_id)
    if biggest_offer is None:
        best_user = -1
        biggest_offer = 0
    elif biggest_offer > 0:
        o = Offer.query.filter_by(price=int(biggest_offer)).first()
        acc_id = o.account_id
        best_user = User.query.get(acc_id)
   
    return render_template("products/product.html", allTags = Tag.query.all(), tags = tags, best_offer = biggest_offer, product = p, best_user = best_user, get_account = User.query.get, get_offers = Offer.by_product, owner = owner)

#Vaihtaa tuotekuvauksen
@app.route("/products/change/description/<product_id>/", methods=["POST"])
@login_required()
def products_set_new_description(product_id):
    p = Product.query.get(product_id)

    if current_user.id == p.account_id or current_user.is_admin():
        p.description = request.form.get("new_description")
        db.session().commit()

    return redirect(url_for("product_index", product_id = product_id))

#Päättää huutokaupan
@app.route("/products/end/<product_id>/", methods=["POST"])
@login_required()
def products_end(product_id):
    p = Product.query.get(product_id)

    if current_user.id == p.account_id or current_user.is_admin():
        p.onSale = False
        db.session().commit()
    
    return redirect(url_for("product_index", product_id = product_id))

#Poistaa tuotteen
@app.route("/products/delete/<product_id>/", methods=["POST"])
@login_required()
def products_delete(product_id):
    p = Product.query.get(product_id)
    offers = Offer.query.filter(Offer.product_id == product_id)
    tps = TagProduct.query.filter(TagProduct.product_id == product_id)
    if current_user.id == p.account_id or current_user.is_admin():
        for offer in offers:
            db.session().delete(offer)
        for tp in tps:
            db.session().delete(tp)
        db.session().delete(p)
        db.session().commit()

    return redirect(url_for("products_index"))

#Lisää tuotteelle tarjouksen
@app.route("/products/offer/<product_id>/", methods=["POST"])
@login_required()
def products_offer(product_id):
    amount = request.form.get("offer")
    p = Product.query.get(product_id)
    biggest_offer = Offer.get_biggest_offer(product_id)
    owner = User.query.get(p.account_id)
    if current_user.id != p.account_id or current_user.is_admin():
        
        if biggest_offer is None or int(amount) > biggest_offer:
             
            o = Offer(amount)
            o.account_id = current_user.id
            o.product_id = product_id
            db.session().add(o)
            db.session().commit()

        else :
            o = Offer.query.filter_by(price=int(biggest_offer)).first()
            acc_id = o.account_id
            best_user = User.query.get(acc_id)
            return render_template("products/product.html", best_user = best_user, best_offer = biggest_offer, owner = owner, e = 1, product = p, get_account = User.query.get, get_offers = Offer.by_product)    
       
    return redirect(url_for("product_index", product_id = product_id))

#Lisää tuotteelle tägin
@app.route("/products/add/tag/<product_id>/", methods=["POST"])
@login_required()
def product_add_tag(product_id):
    p = Product.query.get(product_id)
    if current_user.id == p.account_id or current_user.is_admin():
    
        tag_id = request.form.get("tags")
        tps = TagProduct.query.filter_by(tag_id=tag_id, product_id=product_id).first()
            
        if tps is None:        
            tp = TagProduct(-1, -1)
            tp.product_id = product_id
            tp.tag_id = tag_id
            db.session().add(tp)
            db.session().commit()

    return redirect(url_for("product_index", product_id = product_id))