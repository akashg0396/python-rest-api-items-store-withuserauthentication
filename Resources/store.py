from flask_restful import Resource, reqparse
from Models.store import StoreModel

class Store(Resource):
    def get(self,name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {"message":"store not found"},404

    def post(self,name):
        if StoreModel.find_by_name(name):
            return {'Message':"Store '{}' already present.".format(name)}, 400
        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {"message":"An error occured while inserting a store"},50
        return store.json(),201

    def delete(self,name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
            return {"message":"Store has been deleted"}
        return {"message":"Store not found"}

class StoreList(Resource):
    def get(self):
        stores = StoreModel.find_all()
        return {"stores":[store.json() for store in stores]}
