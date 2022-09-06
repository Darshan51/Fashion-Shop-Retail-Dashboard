from db import db

# from sqlalchemy.orm import relationship

class SaleModel(db.Model):

    __tablename__ = 'sales_data'

    sale_id = db.Column(db.Integer, primary_key=True)
    sale_amount = db.Column(db.Integer)
    sale_date = db.Column(db.String(80))

    product_id = db.Column(db.String(70),db.ForeignKey("products.prod_id"))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id")) 

    # sale_detail = db.relationship("ProductModel",foreign_keys = ['product_id'])
    


    def __init__(self,sale_id,user_id,product_id,sale_amount,sale_date):
        self.sale_id = sale_id
        self.user_id = user_id
        self.product_id = product_id
        self.sale_amount = sale_amount
        self.sale_date = sale_date 
    
    def json(self):
        return { "sale_id":self.sale_id,
            "user_id": self.user_id,
            "product_id": self.product_id,
            "sale_amount": self.sale_amount,
            "sale_date": self.sale_date,}
    
    @classmethod
    def find_by_sale_id(cls,sale_id):
        return cls.query.filter_by(sale_id=sale_id).first()

    def save_to_db(self):

        db.session.add(self)  
        db.session.commit()  

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()    
