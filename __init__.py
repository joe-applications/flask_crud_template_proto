from flask import Flask

from routes import api
from orm import db
from models import (
    Product,
    Cart
)


def create_app():
    app = Flask(__name__)
    app.register_blueprint(api)
    configure_db(app)
    return app


def configure_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:password@172.17.0.3:3306/store"
    db.init_app(app)

    with app.app_context():
        db.create_all()


app = create_app()
