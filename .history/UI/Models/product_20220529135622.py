class product(db.Model):
    Product_Code= db.Column(db.string(15), primary_key= True)
    Warehouse= db.Column(db.string(20), nullable=False)
    Product_Category= db.Column(db.string(20), nullable=False)
    Date= db.Column(db.DateTime, default= datetime.utcnow)
    Order_Demand= db.Column(db.string(200), nullable=False)