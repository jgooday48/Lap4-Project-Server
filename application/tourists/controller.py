from flask import jsonify, request, Flask
from flask_jwt_extended import create_access_token, create_refresh_token, current_user, get_jwt_identity, get_jwt, JWTManager
from .model import Tourist


app = Flask(__name__)
jwt = JWTManager(app)


def register():
    data = request.get_json()

    user = Tourist.get_user_by_username(username=data.get('username'))

    if user is not None:
        return jsonify({"error": 'Tourist already exists'}), 403

    new_user = Tourist(
        username=data.get('username'),
        email=data.get('email'),
        user_type=data.get('user_type'),
        name=data.get('name')
    )

    new_user.set_password(password=data.get('password'))
    new_user.save()
    return jsonify({"message": "User created"}), 201


def login():
    data = request.get_json()

    user = Tourist.get_user_by_username(username=data.get('username'))

    if user and (user.check_password(password=data.get('password'))):
        access_token = create_access_token(identity=user.username)
        refresh_token = create_refresh_token(identity=user.username)

        return jsonify(
            {"message": "Logged in ",
             "tokens": {
                 "access": access_token,
                 "refresh": refresh_token
             }
             }
        ), 200
    return jsonify({"error": "Invalid username or password"}), 400


def find_user(username):

    if username is None:
        return jsonify({"error": "Username parameter is required"}), 403

    user = Tourist.get_user_by_username(username=username)

    if user is not None:
        return jsonify([user.json]), 200
    else:
        return jsonify({"message": "User not found"}), 500


def current_tourist():
    current_identity = get_jwt_identity()
    tourist = Tourist.query.filter_by(username=current_identity).first()

    if tourist:
        return jsonify({
            "message": "User details retrieved successfully",
            "user_details": {"tourist_id": tourist.tourist_id, "username": tourist.username, "email": tourist.email}
        })
    else:
        return jsonify({"message": "User not found"}), 404


def refresh_access():
    identity = get_jwt_identity()
    access_token = create_access_token(identity=identity)
    return jsonify({"access_token": access_token})
