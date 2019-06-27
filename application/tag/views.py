from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application import app, db, login_required
from application.tag.models import Tag
from application.tag.forms import TagForm
from application.tagProduct.models import TagProduct
from application.auth.models import User

@app.route("/tags/", methods=["GET"])
def tags_index():
    return render_template("tag/list.html", tags = Tag.query.all(), form = TagForm())

@app.route("/tags/new", methods=["POST"])
@login_required()
def tags_create():
    form = TagForm(request.form)

    if not form.validate():
        return render_template("tag/list.html", form = form)
    
    t = Tag(form.name.data)

    db.session().add(t)
    db.session().commit()

    return redirect(url_for("tags_index"))

@app.route("/tags/<tag_id>/", methods=["GET"])
def tag_index(tag_id):
    t = Tag.query.get(tag_id)
    products = TagProduct.products_by_tag_id(tag_id)
    return render_template("tag/one.html", tag = t, get_account = User.query.get, products = products)

@app.route("/tags/delete/<tag_id>/", methods=["POST"])
def tag_delete(tag_id):
    t = Tag.query.get(tag_id)
    tps = TagProduct.query.filter(TagProduct.tag_id == tag_id)
    if current_user.is_admin:
        for tp in tps:
            db.session().delete(tp)
        db.session().delete(t)
        db.session().commit()

    return redirect(url_for("tags_index"))