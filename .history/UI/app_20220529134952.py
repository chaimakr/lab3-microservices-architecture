from flask import Flask, render_template , url_for
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///test.db'
db = SQLAlchemy(app)

class product(db.Model):
    Product_Code= db.Column(db.string, primary_key= True)
    Warehouse= db.Column(db.string, primary_key= True)
    Product_Category= db.Column(db.string, primary_key= True)
    Date= db.Column(db.string, primary_key= True)
    Order_Demand= db.Column(db.string, primary_key= True)

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)