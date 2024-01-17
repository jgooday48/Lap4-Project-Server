from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager
from flask_socketio import SocketIO
from .events import socketio

import os


db = SQLAlchemy() # initialise db
jwt = JWTManager()

def create_app(env=None):
    load_dotenv()
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'KEEPITHUSHHUSH'

    CORS(app,resources={r"/*":{"origins":"*"}})

    socketio.init_app(app)

    app.json_provider_class.sort_keys = False
   
    if env == 'TEST':
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        # app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://"
        app.config['SQLALCHEMY_DATABASE_URI']= os.environ['TEST_DB']
    else:
        app.config['TESTING'] = False
        app.config['DEBUG'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ["SQLALCHEMY_DATABASE_URI"]



    db.init_app(app)
    jwt.init_app(app)

    #import blueprints
    from application.routes import main_bp
    from application.tourists.routes import tourist_bp
    from application.guides.routes import guide_bp
    from application.tourists.model import Tourist
    from application.tokens.model import Token
    from application.tokens.routes import token_bp
    from application.places.routes import places_bp
    from application.reviews.routes import reviews_bp
    from application.plans.routes import plans_bp
    from application.activities.routes import activities_bp
    from application.chat.routes import chat_bp
    from application.message.routes import message_bp
    from application.notification.routes import notification_bp
    from application.notes.routes import notes_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(tourist_bp)
    app.register_blueprint(guide_bp)
    app.register_blueprint(token_bp)
    app.register_blueprint(places_bp)
    app.register_blueprint(activities_bp)
    app.register_blueprint(plans_bp)
    app.register_blueprint(reviews_bp)
    app.register_blueprint(chat_bp)
    app.register_blueprint(message_bp)
    app.register_blueprint(notification_bp)
    app.register_blueprint(notes_bp)

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
    

    @jwt.token_in_blocklist_loader
    def token_in_blocklist_callback(jwt_header, jwt_data):
        jti = jwt_data['jti']
        token = db.session.query(Token).filter(Token.jti==jti).scalar()
        return token is not None


    return app

