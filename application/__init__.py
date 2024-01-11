from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager
from flask_socketio import SocketIO, emit


import os


db = SQLAlchemy() # initialise db
jwt = JWTManager()

def create_app(env=None):
    load_dotenv()
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'KEEPITHUSHHUSH'

    CORS(app,resources={r"/*":{"origins":"*"}})
    socketio = SocketIO(cors_allowed_origins="*", async_handlers=True)
    socketio.init_app(app)

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

    @socketio.on("connect")
    def connected():
        print(request.sid)
        emit("connect",{"data": "id is connected"})
        print("client has connected")

    @socketio.on('data')
    def handle_message(data):
        print("data from the front end: ",str(data))
        emit("data",{'data':data},broadcast=True)

    @socketio.on("disconnect")
    def disconnected():
        print("user disconnected")
        emit("disconnect","user disconnected",broadcast=True)


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
    


    


    from application.places.routes import places
    app.register_blueprint(places)

    from application.activities.routes import activities
    app.register_blueprint(activities)

    # from application.plans.routes import plans
    # app.register_blueprint(plans)

    # from application.reviews.routes import reviews
    # app.register_blueprint(reviews)


    return app, socketio

