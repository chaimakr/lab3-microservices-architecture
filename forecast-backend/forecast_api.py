from flask import Flask
from flask_cors import CORS
from pymongo import MongoClient
import os
from dotenv import load_dotenv
from bson.json_util import dumps

app = Flask(__name__)
CORS(app)

load_dotenv()
database_url = os.getenv('MONGO_URL')
client = MongoClient(database_url)
db = client.get_database("lab3-microservices")

#get products from mongo database
@app.route('/products', methods=['GET'])
def list_products():
    response = {}
    products = db.products.find().limit(20)
    data = dumps(products)
    response["data"] = data
    return response

@app.route('/products/<product_code>', methods=['GET'])
def get_product(product_code):
    response = {}
    forecasts = db.products.find({'Product_Code': product_code}).limit(5)
    data = dumps(forecasts)
    response["data"] = data
    return response

app.run(debug=True, port=5002)