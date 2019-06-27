from flask import render_template
from application import app
from application.auth.models import User

@app.route("/")
def index():
    
    return render_template("index.html", min_offer = User.find_offer_min(), offer_average = User.find_offer_average(), max_offer = User.find_price_max(), product_amount=User.find_how_many_products())