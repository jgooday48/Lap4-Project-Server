from flask import jsonify, request, Flask
from flask_jwt_extended import create_access_token, create_refresh_token, current_user, get_jwt_identity, get_jwt, JWTManager
from .model import Tourist
from werkzeug import exceptions
from application.guides.model import Guide



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

    user = Tourist.get_user_by_email(email=data.get('email'))

    if user and (user.check_password(password=data.get('password'))):
        access_token = create_access_token(identity=user.email)
        refresh_token = create_refresh_token(identity=user.email)

        return jsonify(
            {"message": "Logged in ",
             "tokens": {
                 "access": access_token,
                 "refresh": refresh_token
             }
             }
        ), 200
    return jsonify({"error": "Invalid email or password"}), 400


def find_user_by_email(email):

    if email is None:
        return jsonify({"error": "email parameter is required"}), 403

    user = Tourist.get_user_by_email(email=email)

    if user is not None:
        return jsonify([user.json]), 200
    else:
        return jsonify({"message": "User not found"}), 500

def find_user_id(id):
    try:
        user = Tourist.query.filter_by(tourist_id=id)
        return jsonify([tourist.json for tourist in user]), 200
    
    except Exception as e:
        print(str(e))
        return jsonify({"error": "Error: Tourist cannot be retrieved"}), 400


def find_user_by_username(username):

    if username is None:
        return jsonify({"error": "email parameter is required"}), 403

    user = Tourist.get_user_by_username(username=username)

    if user is not None:
        return jsonify([user.json]), 200
    else:
        return jsonify({"message": "User not found"}), 500

def current_tourist():
    current_identity = get_jwt_identity()
    tourist = Tourist.query.filter_by(email=current_identity).first()

    if tourist:
        return jsonify({
            "message": "User details retrieved successfully",
            "user_details": {"user_type": tourist.user_type.name, "tourist_id": tourist.tourist_id, "username": tourist.username, "email": tourist.email}
        })
    else:
        return jsonify({"message": "User not found"}), 404


def refresh_access():
    identity = get_jwt_identity()
    access_token = create_access_token(identity=identity)
    return jsonify({"access_token": access_token})


def index():
    tourists = Tourist.query.all()

    try:
        return jsonify({"all_guides": [t.json for t in tourists]})
    except:
        raise exceptions.InternalServerError(
            f"Server is down. We are fixing it")


def find_guides_by_tourist(id): 
    try:
        tourist = Tourist.query.filter_by(tourist_id=id).first()

        if tourist: 
            tourist_guides = tourist.get_guides()
            return jsonify(tourist_guides), 200
        else:
            return jsonify({"error": "Tourist not found"}), 404
    
    except Exception as e:
        print(str(e))


def join_tourist_and_guide():
    data = request.json

    tourist_id = data.get('tourist_id')
    guide_id = data.get('guide_id')

    if not guide_id or not tourist_id:
        return jsonify({'error': 'Guide ID and Tourist ID are required'}), 400


    guide = Guide.query.get(guide_id)

    if not guide:
        return jsonify({'error': 'Guide not found'}), 404


    tourist = Tourist.query.get(tourist_id)

    if not tourist:
        return jsonify({'error': 'Tourist not found'}), 404


    tourist.add_guide(guide)

    return jsonify({'message': 'Tourist and Guide paired up successfully'}), 200


def remove_tourist_guide_pair(tourist_id, guide_id):
    try:

        # Check if both tourist_id and guide_id are provided as query parameters
        if not tourist_id or not guide_id:
            return jsonify({"error": "Both tourist_id and guide_id must be provided as query parameters"}), 400

        tourist = Tourist.query.get(tourist_id)
        guide = Guide.query.get(guide_id)


        if not tourist or not guide:
            return jsonify({"error": "Tourist or guide not found"}), 404

        tourist.remove_guide(guide)

        return jsonify({"message": f"Guide with ID {guide_id} removed from tourist with ID {tourist_id}"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

