from email.policy import default
from flask import Flask, render_template , url_for
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy 
from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///test.db'
db = SQLAlchemy(app)

class product(db.Model):
    Product_Code= db.Column(db.String(15), primary_key= True)
    Warehouse= db.Column(db.String(20), nullable=False)
    Product_Category= db.Column(db.String(20), nullable=False)
    Date= db.Column(db.DateTime, default= datetime.utcnow)
    Order_Demand= db.Column(db.String(200), nullable=False)

    def __repr__(self) -> str:
        return '<product %p>' % self.id 

@app.route("/")
def index():
    return render_template('product.html')

if __name__ == "__main__":
    app.run(debug=True)