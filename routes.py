from flask import Blueprint
from orm import db
from models import Product, Cart


api = Blueprint('api', __name__)


@api.route('/')
def index():
    return {'msg': 'Endpoint - index'}


@api.route('/add')
def add_product():
    product = Product(name="Milk", price=2.50)
    try:
        db.session.add(product)
        db.session.commit()
    except Exception as e:
        print(e)
        return {'msg': 'Insert failed'}
    return {'msg': 'Insert Successful!'}
