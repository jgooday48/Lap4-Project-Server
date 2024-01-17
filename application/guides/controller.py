from flask import jsonify, request
from flask_jwt_extended import create_access_token, create_refresh_token, current_user, get_jwt_identity, get_jwt
from .model import Guide
from werkzeug import exceptions
from application.activities.model import Activity
from .. import db

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

    user = Guide.get_user_by_email(email=data.get('email'))

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
        return jsonify({"error": "Email parameter is required"}), 403

    user = Guide.get_user_by_email(email=email)
    if user is not None:
        return jsonify([user.json]), 200
    else:
        return jsonify({"message": "User not found"}), 500
    


def update(id):
    try:
        data = request.json
        guide = Guide.query.filter_by(guide_id=id).first()

        if guide is None:
            raise exceptions.NotFound("Guide does not exist")

        # Check if 'filters' key exists in the request data
        if 'filters' in data:
            new_filters = set(data['filters'])

            # Keep activities that have at least one matching filter
            guide.activities = [
                activity for activity in guide.activities if any(
                    filter in new_filters for filter in activity.filters
                )
            ]

            # Get new matching activities
            matching_activities = Activity.query.filter(
                Activity.filters.overlap(new_filters)).all()

            # Add new matching activities to the guide
            for activity in matching_activities:
                if activity not in guide.activities:
                    guide.activities.append(activity)

        # Update other attributes
        for (attribute, value) in data.items():
            if hasattr(guide, attribute):
                setattr(guide, attribute, value)

        # Commit the changes
        db.session.commit()

        return jsonify({"data": guide.json}), 201

    except Exception as e:
        db.session.rollback()
        raise exceptions.InternalServerError(f"Error updating guide: {str(e)}")





# def find_user(username):

#     if user is not None:
#         return jsonify([user.json]), 200
#     else:
#         return jsonify({"message": "User not found"}), 500
    
def find_user_by_username(username):

    if username is None:
        return jsonify({"error": "username parameter is required"}), 403

    user = Guide.get_user_by_username(username=username)

    if user is not None:
        return jsonify([user.json]), 200
    else:
        return jsonify({"message": "User not found"}), 500

def current_guide():
    current_identity = get_jwt_identity()
    guide = Guide.query.filter_by(email=current_identity).first()

    if guide:
        return jsonify({
            "message": "User details retrieved successfully",
            "user_details": {"user_type":guide.user_type.name ,"guide_id": guide.guide_id, "email": guide.email, "guide_Username": guide.username}
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
    try:
         guide= Guide.query.filter_by(guide_id=id)
         return jsonify([guides.json for guides in guide]), 200

    except:
        raise exceptions.NotFound(f"guide does not exist")



def find_activities_by_guide(id):
    try:
        guide = Guide.query.filter_by(guide_id=id).first()
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
