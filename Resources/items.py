import json
from flask_restful import Resource, Api,reqparse
from flask_jwt import jwt_required
from Models.item import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
    type=float,
    required=True,
    help="This field cannot be left blank"
    )

    parser.add_argument('store_id',
    type=int,
    required=True,
    help="Every item needs a store id"
    )

    @jwt_required()
    def get(self,name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {"message":"item not found"},404

    def post(self,name):
        if ItemModel.find_by_name(name):
            return {'Message':"Item '{}' already present in store".format(name)}, 400
        else:
            data = Item.parser.parse_args() #get_json(force=true) does not require content type
            new_item = ItemModel(name,**data)
            try:
                new_item.save_to_db()
            except:
                return {"message":"An error occured while inserting item"},500
            return new_item.json(),201

    def put(self,name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)
        if item:
            item.price = data['price']
        else:
            item = ItemModel(name,**data)
        item.save_to_db()
        return item.json()

    def delete(self,name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        return {"message":"Item has been deleted"}

class ItemList(Resource):
    def get(self):
        items =  ItemModel.find_all()
        return {"items":[item.json() for item in items]}
