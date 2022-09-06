from flask import Flask
from flask_cors import CORS
from flask_jwt import JWT
from flask_restful import Api

from db import db
from resources.products import Product
from resources.sales import (Avg_sale, Product_sale_details, Sale, SaleList,
                             Total_profit, Total_sale, Total_visitors)
from resources.users import Getuser, UserRegister
from security import authenticate, identity

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

app.config["SQLACHEMY_TRACK_MODIFICATION"] = False

app.secret_key = "darshan"

CORS(app)

api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


# @app.after_request
# def after_request(response):
#     response.headers.add("Access-Control-Allow-Origin", "*")
#     response.headers.add(
#         "Access-Control-Allow-Headers", "Content-Type,Authorization"
#     )
#     response.headers.add(
#         "Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS"
#     )
#     return response


jwt = JWT(app, authenticate, identity)

api.add_resource(Product, "/product/<string:prod_id>")
api.add_resource(Sale, "/sale/<int:sale_id>")
api.add_resource(SaleList, "/sale_list")
api.add_resource(Total_visitors, "/total_visitors")
api.add_resource(Total_sale, "/total_sale")
api.add_resource(Avg_sale, "/avg_sale")
api.add_resource(Getuser,"/username/<string:username>")
api.add_resource(Product_sale_details,"/sale_details")
api.add_resource(Total_profit, "/total_profit")
api.add_resource(UserRegister, "/register_user")


if __name__ == "__main__":

    db.init_app(app)
    app.run(port=5000, debug=True)
