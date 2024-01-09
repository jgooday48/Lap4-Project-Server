from flask import Flask, jsonify
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
    from application.guides.routes import guide_bp
    from application.tourists.model import Tourist


    app.register_blueprint(main)
    app.register_blueprint(tourist_bp)
    app.register_blueprint(guide_bp)

    @jwt.user_lookup_loader
    def user_lookup_callback(_jwt_headers, jwt_data):
        identity = jwt_data['sub']
        return Tourist.query.filter_by(username=identity).one_or_none



    #jwt error handlers
    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_data): 
        return jsonify({'message':'Token has expired', 'error': 'Token expired'}), 401
    
    @jwt.expired_token_loader
    def invalid_token_callback(error):
        return jsonify({'message': 'Signature verificatoin failed', 'error': 'Invalid token'}), 401
    
    @jwt.expired_token_loader
    def missing_token_callback(error):
        return jsonify({'message': 'Request does not contain valid token', 'error': 'authorization_header'}), 401
    


    


    return app

