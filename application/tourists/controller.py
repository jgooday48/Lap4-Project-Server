from flask import jsonify, request 
from flask_jwt_extended import create_access_token, create_refresh_token
from .model import Tourist


def register():
    data = request.get_json()

    user = Tourist.get_user_by_username(username = data.get('username'))

    if user is not None:
        return jsonify({"error": 'Tourist already exists'}), 403
    
    new_user = Tourist(
        username = data.get('username'),
        email = data.get('email'),
        user_type = data.get('user_type'),
        name = data.get('name')
    )

    new_user.set_password(password = data.get('password'))
    new_user.save()
    return jsonify({"message": "User created"}), 201

def login(): 
    data = request.get_json()

    user = Tourist.get_user_by_username(username=data.get('username'))
    
    if user and (user.check_password(password=data.get('password'))):
        access_token = create_access_token(identity=user.username)
        refresh_token = create_refresh_token(identity=user.username)

        return jsonify(
            {"message":"Logged in ",
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


