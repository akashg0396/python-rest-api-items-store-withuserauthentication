from flask_restful import Resource, reqparse
from Models.user import UserModel

class UserRegistration(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
    type=str,
    required=True,
    help="This field cannot be left blank"
    )

    parser.add_argument('password',
    type=str,
    required=True,
    help="This field cannot be left blank"
    )


    def post(self):
        data = UserRegistration.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "User with this username already exists"}, 409

        user =  UserModel(**data)
        user.save_to_db()

        return {"message": "User created successfully"}, 201

class User(Resource):
    @classmethod
    def get(cls, user_id):
        user = UserModel.find_by_id(user_id)
        if user:
            return user.json()
        return {"message":"User not found"},404
        

    @classmethod
    def delete(cls, user_id):
        user = UserModel.find_by_id(user_id)
        if user:
            user.delete_from_db()
            return {"message":"User deleted successfully"},200
        return {"message":"User not found"},404