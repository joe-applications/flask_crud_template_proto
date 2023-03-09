from orm import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)
    cart_id = db.Column(db.Integer, db.ForeignKey('cart.id'))


class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    products = db.relationship('Product', backref='cart')
