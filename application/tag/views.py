from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application import app, db, login_required
from application.tag.models import Tag
from application.tag.forms import TagForm

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
