#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate
from flask_restful import Resource, Api
from sqlalchemy import desc
from models import Bakery

from models import db, Bakery, BakedGood

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

api = Api(app)

@app.route('/')
def index():
    return '<h1>Bakery GET API</h1>'

class Home(Resource):
    def get(self):
        bakeries = Bakery.query.all()
        bakery_names = [bakery.to_dict() for bakery in bakeries]
        response = make_response(bakery_names, 200)
        return response

api.add_resource(Home, '/bakeries')


class GetBakery(Resource):
    def get(self, id):
        bakery =  Bakery.query.filter_by(id = id).first()
        response = make_response(bakery.to_dict(), 200)

        return response

api.add_resource(GetBakery, '/bakeries/<int:id>')

    
        

class GoodsPrice(Resource):
    def get(self):
        goods = BakedGood.query.order_by(desc("price"))
        prices = [item.to_dict() for item in goods]
        response = make_response(prices, 200)

        return response

api.add_resource(GoodsPrice, '/baked_goods/by_price')

class MostExpensive(Resource):
    def get(self):
        goods = BakedGood.query.order_by(desc("price")).first()
        response = make_response(goods.to_dict(), 200)

        return response

api.add_resource(MostExpensive, '/baked_goods/most_expensive')
    





def most_expensive_baked_good():
   pass

if __name__ == '__main__':
    app.run(port=5555, debug=True)
