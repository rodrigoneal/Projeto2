from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import filtros

db = SQLAlchemy()




def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:/// app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'secreto'
    app.jinja_env.filters['formatdate'] = filtros.formatar_data
    app.jinja_env.filters['parser_seconds'] = filtros.seconds_to_time
    db.init_app(app)
    from .routes import init_routes
    init_routes(app, db)

    return app
