from flask import jsonify, request 
from .model import Tourist


def register():
    data = request.get_json()

    user = Tourist.get_user_by_username(username = data.get('username'))

    if user is not None:
        return jsonify({"error": 'Tourist already exists'})
    
    new_user = Tourist(
        username = data.get('username'),
        email = data.get('email'),
        user_type = data.get('user_type'),
        name = data.get('name')
    )

    new_user.set_password(password = data.get('password'))
    new_user.save()
    return jsonify({"message": "User created"})

def find_user(username):
    # username = request.args.get('username')

    if username is None:
        return jsonify({"error": "Username parameter is required"})

    user = Tourist.get_user_by_username(username=username)

    if user is not None:
        return jsonify([user.json])
    else:
        return jsonify({"message": "User not found"})


