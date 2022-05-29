from email.policy import default
from flask import Flask, render_template , url_for
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy 
from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///test.db'
db = SQLAlchemy(app)

class product(db.Model):
    Product_Code= db.Column(db.string(15), primary_key= True)
    Warehouse= db.Column(db.string(20), nullable=False)
    Product_Category= db.Column(db.string(20), nullable=False)
    Date= db.Column(db.DateTime, default= datetime.utcnow)
    Order_Demand= db.Column(db.string(200), nullable=False)

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)