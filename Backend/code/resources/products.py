from flask_jwt import jwt_required
from flask_restful import Resource, reqparse
from models.product import ProductModel


class Product(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "prod_id",
        type=str,
        required =True,
        help = "Please provide the product id of product"
    )
    parser.add_argument(
        "prod_name",
        type=str,
        required =True,
        help = "Please provide the product name of product"
    )
    parser.add_argument(
        "cost_price",
        type=float,
        required =True,
        help = "Please provide the product cost price of product"
    )
    parser.add_argument(
        "desc",
        type=str
    )

    @jwt_required()
    def get(self,prod_id):
        product = ProductModel.find_by_prod_id(prod_id)
        if product:
            return product.json()
        return {"message":"Product is not found"},404
    
    @jwt_required()
    def post(self,prod_id):
        if ProductModel.find_by_prod_id(prod_id):
            return {"message": "A product with '{}' already exist".format(prod_id)}

        data = Product.parser.parse_args()
        product = ProductModel(
                            data["prod_id"],
                            data["desc"],
                            data['prod_name'],
                            data['cost_price']
                         )
        try:
            product.save_to_db()
        except:
            return {"message": "An internal error occcured"} , 500   
        
        return product.json()
    
    @jwt_required()
    def delete(self,prod_id):
        product = ProductModel.find_by_prod_id(prod_id)
        if product:
            product.delete_from_db()
        return {"message": "product deleted"}
    
    @jwt_required()
    def put(self,prod_id):
        request_data = Product.parser.parse_args()

        product = ProductModel.find_by_prod_id(prod_id)

        if product is None:  
            #Create a new product
            product = ProductModel(
                request_data["prod_id"],
                request_data["desc"],
                request_data['prod_name'],
                request_data['cost_price']
            )
        else:
            # update the existing product
            product.cost_price = request_data["cost_price"]

        product.save_to_db()

        return product.json()

class ProductList(Resource):
    @jwt_required()
    def get(self):
        return {"Product List":[product.json() for product in ProductModel.query().all()]}
