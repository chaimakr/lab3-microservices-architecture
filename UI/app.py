from email.policy import default
import json
from flask import Flask, render_template , url_for
# from flask_sqlalchemy import SQLAlchemy
# import sqlalchemy 
from datetime import datetime

import requests
app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///test.db'
# db = SQLAlchemy(app)

# class product(db.Model):
#     Product_Code= db.Column(db.String(15), primary_key= True)
#     Warehouse= db.Column(db.String(20), nullable=False)
#     Product_Category= db.Column(db.String(20), nullable=False)
#     Date= db.Column(db.DateTime, default= datetime.utcnow)
#     Order_Demand= db.Column(db.String(200), nullable=False)

#     def __repr__(self) -> str:
#         return '<product %p>' % self.id 

BASE_URL = "http://127.0.0.1:5002/"
@app.route("/")
def index():
    return render_template('product.html')

@app.route("/products")
def get_all_products():
    response = requests.get(BASE_URL + "products/")
    products = json.loads(response.data)

@app.route("/products/<string:code>")
def get_product(code):
    response = requests.get(BASE_URL + "products/" + code)
    print(response.text)
    products = json.loads(response.data)
    return render_template('product-info.html', products=products[0])

if __name__ == "__main__":
    app.run(debug=True)