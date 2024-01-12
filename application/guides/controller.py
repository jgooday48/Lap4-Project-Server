from flask import jsonify, request
from flask_jwt_extended import create_access_token, create_refresh_token, current_user, get_jwt_identity, get_jwt
from .model import Guide
from werkzeug import exceptions
from application.activities.model import Activity


def register():
    data = request.get_json()

    user = Guide.get_user_by_username(username=data.get('username'))

    if user is not None:
        return jsonify({"error": 'Guide already exists'}), 403

    new_user = Guide(
        username=data.get('username'),
        place_id = data.get('place_id'),
        email=data.get('email'),
        user_type=data.get('user_type'),
        name=data.get('name'),
        filters=data.get('filters'),
        availible_from = data.get('availible_from'),
        availible_to = data.get('availible_to')
    )

    new_user.set_password(password=data.get('password'))
    new_user.save()
    return jsonify({"message": "New Guide created"}), 201


def login():
    data = request.get_json()

    user = Guide.get_user_by_username(username=data.get('username'))

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

    user = Guide.get_user_by_username(username=username)

    if user is not None:
        return jsonify([user.json]), 200
    else:
        return jsonify({"message": "User not found"}), 500
    

def current_guide():
    current_identity = get_jwt_identity()
    guide = Guide.query.filter_by(username=current_identity).first()

    if guide:
        return jsonify({
            "message": "User details retrieved successfully",
            "user_details": {"username": guide.username, "email": guide.email}
        })
    else:
        return jsonify({"message": "User not found"}), 404
    

def refresh_access():
    identity = get_jwt_identity()
    access_token = create_access_token(identity=identity)
    return jsonify({"access_token": access_token})


def index():
    guides = Guide.query.all()

    try:
        return jsonify({"all guides": [g.json for g in guides]})
    except:
        raise exceptions.InternalServerError(
            f"Server is down. We are fixing it")
    

def find_guide_by_index(id):
    guide= Guide.query.filter_by(guide_id=id).first()
    try:
        return jsonify({"data": guide.json}), 200
    except:
        raise exceptions.NotFound(f"guide does not exist")



def find_activities_by_guide(username):
    try:
        guide = Guide.query.filter_by(username=username).first()
        print("guide: ", guide)

        if guide:
            guide_activities = guide.get_activities()
            return jsonify(guide_activities), 200
        else:
            return jsonify({"error": "Guide not found"}), 404

    except Exception as e:
        print(str(e))
        return jsonify({"error": "Error retrieving activities by guide"}), 500


def add_activity_to_guide():
    data = request.json

    guide_id = data.get('guide_id')
    activity_id = data.get('activity_id')

    if not guide_id or not activity_id:
        return jsonify({'error': 'Guide ID and Activity ID are required'}), 400

    # Check if the guide with the given ID exists
    guide = Guide.query.get(guide_id)

    if not guide:
        return jsonify({'error': 'Guide not found'}), 404

    # Check if the activity with the given ID exists
    activity = Activity.query.get(activity_id)

    if not activity:
        return jsonify({'error': 'Activity not found'}), 404

    # Add the activity to the guide
    guide.add_activity(activity)

    return jsonify({'message': 'Activity and Guide paired up successfully'}), 200


def guides_by_place_id(place_id):
    try: 
        guides = Guide.query.filter_by(place_id=place_id).all()
        return jsonify([g.json for g in guides]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
