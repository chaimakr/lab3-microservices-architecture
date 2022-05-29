from flask import Flask
from pymongo import MongoClient
import os
from dotenv import load_dotenv
from bson.json_util import dumps

app = Flask(__name__)

load_dotenv()
database_url = os.getenv('MONGO_URL')

#get products from mongo database
@app.route('/products', methods=['GET'])
def list_products():
    client = MongoClient(database_url)
    db = client.forecast_db
    response = {}
    products = db.products.find()
    data = dumps(products)
    response["data"] = data
    return response

@app.route('/products/<product_code>', methods=['GET'])
def get_product(product_code):
    client = MongoClient(database_url)
    db = client.forecast_db
    response = {}
    forecasts = db.products.find({'Product_Code': product_code})
    data = dumps(forecasts)
    response["data"] = data
    return response

app.run(debug=True, port=5000)