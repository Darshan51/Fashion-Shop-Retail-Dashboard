# from flask_jwt import jwt_required
from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "firstname",
        type=str,
        required=True,
        help="Please provide firstname of the user",
    )
    parser.add_argument(
        "lastname",
        type=str,
        required=True,
        help="Please provide lastname of the user",
    )
    parser.add_argument(
        "username",
        type=str,
        required=True,
        help="username field can not be empty",
    )
    parser.add_argument(
        "password", type=str, required=True, help="password is required"
    )

    def post(self):
        data = UserRegister.parser.parse_args()
        if UserModel.find_by_username(data["username"]):
            return {"message": "A user with that username already exist"}, 200
        user = UserModel(
            **data
        )  # user = UserModel(data['firstname'],data['lastname'],.....)
        user.save_to_db()

        return {"message": "User is created successfully"}, 201
    
class Getuser(Resource):
    def get(self,username):
        user = UserModel.find_by_username(username)
        if user : return {"username":user.username,"firstname":user.firstname}
        return {"message":"user does not exitst"}
    
    def delete(self,username):
        user = UserModel.find_by_username(username)
        if user : user.delete_from_db()
        return {"message":"user deleted successfully"}
