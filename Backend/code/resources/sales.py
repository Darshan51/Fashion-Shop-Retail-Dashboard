
import json

from db import db
from flask_jwt import jwt_required
from flask_restful import Resource, reqparse
from models.product import ProductModel
from models.sale import SaleModel
from sqlalchemy.sql import func


class Sale(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "user_id",
        type=int,
        required=True,
        help="this field cannot be empty",
    )
    parser.add_argument(
        "product_id",
        type=str,
        required=True,
        help="this field cannot be empty",
    )
    parser.add_argument(
        "sale_amount",
        type=int,
        required=True,
        help="this field cannot be empty",
    )
    parser.add_argument(
        "date",
        type=str,
        required=True,
        help="this field cannot be empty",
    )
    
    @jwt_required()
    def get(self,sale_id):
        sale = SaleModel.find_by_sale_id(sale_id)
        if sale:
            return sale.json() , 201
        return {"message":"There is no sale with that sale_id"},400 

    @jwt_required()
    def post(self,sale_id):
        if SaleModel.find_by_sale_id(sale_id):
            return {
                "message": "sale data with sale id {} already exist".format(sale_id)
            }, 400

        data = Sale.parser.parse_args()
        sale = SaleModel(
           sale_id,
           data["user_id"],
           data["product_id"],
           data["sale_amount"],
           data["date"],
        )

        try:
            sale.save_to_db()
            return {"message":"sale is added to the sales table"},201
            
        except:
            return {
                "message": "An error occured while saving the sales data"
            }, 500  # internal server error

    @jwt_required()
    def delete(self,sale_id):
        item = SaleModel.find_by_sale_id(sale_id)
        if item:
            item.delete_from_db()
        return {"message": "sales_data_deleted"}

    @jwt_required()    
    def put(self,sale_id):
        request_data = Sale.parser.parse_args()

        item = SaleModel.find_by_sale_id(sale_id)

        if item is None:
            item = SaleModel(
                sale_id,
                request_data["user_id"],
                request_data["product_id"],
                request_data["sale_amount"],
                request_data["date"],
            )
        else:

            item.user_id = request_data["user_id"]
            item.product_id = request_data["product_id"]
            item.sale_amount = request_data["sale_amount"]
            item.date = request_data["date"]
        item.save_to_db()

        return item.json()


class SaleList(Resource):
    @classmethod
    @jwt_required()
    def get(cls):
        res = [sale.json() for sale in SaleModel.query.all()]
        return {"SaleList": res }


class Total_sale(Resource):
    @classmethod
    @jwt_required()
    def get(cls):
        res = SaleModel.query.with_entities(func.sum(SaleModel.sale_amount)).first()
        return {"total_sale" : res[0]}   


class Total_visitors(Resource):
    @classmethod
    @jwt_required()
    def get(cls):
        res = SaleModel.query.with_entities(func.count(SaleModel.user_id)).first()
        return {"total_visitors" : res[0]}


class Avg_sale(Resource):
    @classmethod
    @jwt_required()
    def get(cls):
        return float((Total_sale.get())/(Total_visitors.get()))
        

class Product_sale_details(Resource):
   @classmethod
   @jwt_required()
   def get(cls):
      
        res = db.session.query(
            ProductModel.prod_id, ProductModel.prod_name,ProductModel.desc,SaleModel.sale_amount,
            ((SaleModel.sale_amount - ProductModel.cost_price)/ProductModel.cost_price).label("profit")
            ).filter( SaleModel.product_id== ProductModel.prod_id
            ).all()
        result = []
        
        for x in res:
            temp = {
                'prod_id':x[0],
                'prod_name' : x[1],
                'desc' : x[2],
                'sale_amount' : x[3],
                'profit' : round(x[4],2)

            }
            result.append(temp)
    
        return {"sale_details" : result}

class Total_profit(Resource):
    @classmethod
    @jwt_required()
    def get(cls):
        res = db.session.query(func.sum((SaleModel.sale_amount - ProductModel.cost_price
        )/(ProductModel.cost_price))
        ).filter( SaleModel.product_id== ProductModel.prod_id).all()
        
        temp = round(res[0][0],2)

        return {"total_profit" : temp}
