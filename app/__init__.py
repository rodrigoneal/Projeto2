from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()




def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:/// app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'secreto'
    db.init_app(app)
    from .routes import init_routes
    init_routes(app, db)

    return app
