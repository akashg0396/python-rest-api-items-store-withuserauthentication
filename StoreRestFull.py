import os
from flask import Flask, request
from flask_restful import  Api
from flask_jwt import JWT
from Security import authenticate,identity
from Resources.User import UserRegistration , User
from Resources.items import Item,ItemList
from Resources.store import Store,StoreList

from db import db
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL','sqlite:///data.db') # DATABASE_URL is env var for postgres that we get from heroku however if this var is not present it will take second arg into consideration i.e sqlite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #SQLAlchemy has its own modification tracker so turning off flask modification tracker
app.config['PROPAGATE_EXCEPTION'] = True
app.secret_key='jose'
api = Api(app)

app.config['JWT_AUTH_URL_RULE'] = '/login'
db.init_app(app)
@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app,authenticate,identity)
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegistration, '/registration')
api.add_resource(User, '/user/<int:user_id>')

if __name__ == '__main__':

    app.run(port=7800, debug=True)
