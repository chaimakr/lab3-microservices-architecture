from email.policy import default
from functools import reduce
import json
from datetime import datetime as dt
from flask import Flask, render_template , url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
import sqlalchemy 
from datetime import datetime
from flask import request
import requests

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///test.db'
db = SQLAlchemy(app)
sess = Session(app)

# class product(db.Model):
#     Product_Code= db.Column(db.String(15), primary_key= True)
#     Warehouse= db.Column(db.String(20), nullable=False)
#     Product_Category= db.Column(db.String(20), nullable=False)
#     Date= db.Column(db.DateTime, default= datetime.utcnow)
#     Order_Demand= db.Column(db.String(200), nullable=False)

#     def __repr__(self) -> str:
#         return '<product %p>' % self.id 

def greater_date(date1, date2):
    a = dt.strptime(date1, "%Y/%m/%d")
    b = dt.strptime(date2, "%Y/%m/%d")
    if a > b:
        return date1
    else:
        return date2

@app.route("/")
def index():
    return render_template('home.html')

# @app.route("/products")
# def products():
#     if('username' in session):
#         return render_template('product.html')
#     else:
#         return render_template('login.html')

@app.route("/login", methods=['GET'])
def login_get():
    if('username' in session):
        return render_template('product.html')
    else:
        return render_template('login.html')

@app.route("/login",methods=['POST'])
def login_post():
    res = requests.post('http://localhost:5000/', json={'username':request.form['username'], 'password':request.form['password']})
    if(res.status_code==200):
        session['username'] = request.form['username']
        return render_template('product.html')
    else:
        return render_template('login.html')

@app.route("/logout")
def logout():
    session.pop('username')
    return render_template('login.html')

@app.route("/products", methods=['GET'])
def products_get():
    if('username' in session):
        res = requests.get('http://localhost:5002/products')
        data = json.loads(res.text)
        products = json.loads(data["data"])
        return render_template('product.html', products=products)
    else:
        return render_template('login.html')

@app.route("/products/<product_code>", methods=['GET'])
def products_get_product(product_code):
    if('username' in session):
        res = requests.get('http://localhost:5002/products/'+product_code)
        data = json.loads(res.text)
        products = json.loads(data["data"])
        print(products)
        product = {}
        product["Product_Code"] = products[0]["Product_Code"]
        product["Warehouse"] = products[0]["Warehouse"]
        product["Product_Category"] = products[0]["Product_Category"]
        product["Latest_Date"] = reduce(greater_date, [product["Date"] for product in products])
        product["Order_Demand_Total"] = sum(int(product["Order_Demand"]) for product in products)
        return render_template('product-info.html', product=product)
    else:
        return render_template('login.html')

if __name__ == "__main__":
    app.secret_key = 'BAD_cxvxcvSECRET_KEY'
    app.config['SESSION_TYPE'] = 'filesystem'

    sess.init_app(app)
    app.run(debug=True, port=4999)