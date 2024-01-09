from flask import jsonify, request
from flask_jwt_extended import create_access_token, create_refresh_token, current_user, get_jwt_identity, get_jwt
from .model import Tourist
from ..tokens.model import get_token_model

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
    return jsonify({"message": "message", "user_details": {"username": current_user.username, "email": current_user.email} })


def refresh_access():
    identity = get_jwt_identity()
    access_token = create_access_token(identity=identity)
    return jsonify({"access_token": access_token})


def logout():
    jwt = get_jwt()
    Token = get_token_model()
    jti = jwt['jti']
    token = Token(jti=jti)
    token.save()
    return jsonify({'message': 'Logged out successfully'}), 200

