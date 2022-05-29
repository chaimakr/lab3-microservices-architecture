import os
from dotenv import load_dotenv
from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse
from pymongo import MongoClient

client = MongoClient('localhost:27017')

load_dotenv()
database_url = os.getenv('MONGO_URL')

uri = "mongodb://localhost:27017/"
client = MongoClient(database_url)
db = client.get_database("lab3-microservices")
users = db.get_collection("users")

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument('username', type=str, help='User name is required', required=True)
parser.add_argument('password', type=str, help='User password is required', required=True)

class AuthService(Resource):
    def post(self):
        args = parser.parse_args()
        user = users.find_one({'username': args['username']})
        if(user):
            if(args['password']==user['password']):
                return {"username": user['username']}
            else:
                return "Wrong password", 401
        else:
            return "User not found", 401

api.add_resource(AuthService, '/')

if __name__ == '__main__':
    app.run(debug=True)