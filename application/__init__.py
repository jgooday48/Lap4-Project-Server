from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager
import os


db = SQLAlchemy() # initialise db
jwt = JWTManager()

def create_app(env=None):
    load_dotenv()
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'KEEPITHUSHHUSH'

    app.json_provider_class.sort_keys = False
    CORS(app)
    if env == 'TEST':
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://"
    else:
        app.config['TESTING'] = False
        app.config['DEBUG'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ["SQLALCHEMY_DATABASE_URI"]

    
    db.init_app(app)
    jwt.init_app(app)

    #import blueprints
    from application.routes import main
    from application.tourists.routes import tourist_bp

    app.register_blueprint(main)
    app.register_blueprint(tourist_bp)




    return app

