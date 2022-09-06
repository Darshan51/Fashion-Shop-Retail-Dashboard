from db import db
from sqlalchemy import Column, ForeignKey, Integer, String


class ProductModel(db.Model):
    # Define the table so that SQLALCHEMY can take reference
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key = True)
    prod_id = db.Column(db.String(70))
    desc = db.Column(db.String(90))
    prod_name = db.Column(db.String(70))
    cost_price = db.Column(db.Float)
 

    def __init__(self,prod_it,desc,prod_name,cost_price):
        self.prod_id = prod_it
        self.desc = desc
        self.prod_name = prod_name
        self.cost_price = cost_price
    
    def json(self):
        return {"prod_id":self.prod_id,"description":self.desc,
        "prod_name":self.prod_name,"cost_price":self.cost_price}

    @classmethod
    def find_by_prod_id(cls,prod_id):
        return cls.query.filter_by(prod_id=prod_id).first()

    def save_to_db(self):

        db.session.add(self) 
        db.session.commit()  

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
