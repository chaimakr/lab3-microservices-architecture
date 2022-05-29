import csv
import os
from pymongo import MongoClient
from dotenv import load_dotenv


load_dotenv()

client = MongoClient(os.getenv('MONGO_URL'))
db = client.forecast_db

# save products.csv content to database
def initialize_database():
    with open('csv/products.csv', 'r') as f:
        csv_reader = csv.reader(f, delimiter=',')
        next(csv_reader, None)
        for line in csv_reader:
            db.products.insert_one({
                'Product_Code': line[0],
                'Warehouse': line[1],
                'Product_Category': line[2],
                'Date': line[3],
                'Order_Demand': line[4]
            })

if __name__ == '__main__':
    initialize_database()
