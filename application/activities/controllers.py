from flask import jsonify, request
from werkzeug import exceptions
from .model import Activity
from application.places.model import Place

from .. import db


def index(): 
    activities = Activity.query.all()

    try:
        return jsonify({"all_activities": [a.json for a in activities]})
    except:
        raise exceptions.InternalServerError(
            f"Server is down. We are fixing it")


def show(id):
    print("Activity id: ", type(id))
    activity = Activity.query.filter_by(activity_id=id).first()
    try:
        return jsonify([activity.json]), 200
    except:
        raise exceptions.NotFound(f"Activity not found")
    

def create():
    try:
        data = request.json

   
        name = data.get('name')
        location = data.get('location')
        filters = data.get('filters', [])
        place_id = data.get('place_id')
        description = data.get('description')
        zip_code = data.get('zip_code')
        images = data.get('images', [])


        new_activity = Activity(
            name=name,
            location=location,
            filters=filters,
            place_id=place_id,
            description=description,
            zip_code=zip_code,
            images=images
        )

        db.session.add(new_activity)
        db.session.commit()

        return jsonify(new_activity.json), 201

    except Exception as e:
        print(str(e))
        return jsonify({"error": "Error: Activity cannot be posted"}), 400


def update(id):
    try:
        data = request.json
        activity = Activity.query.filter_by(activity_id=id).first()

        for (attribute, value) in data.items():
            if hasattr(activity, attribute):
                setattr(activity, attribute, value)

        db.session.commit()
        return jsonify({"updated activity": activity.json})
    except:
        raise exceptions.NotFound(f"Activity not found")




def find_guides_by_activity(id):
    try:
        activity = Activity.query.filter_by(activity_id=id).first()
        print("activity: ", activity)

        if activity:
            activity_guides = activity.get_guides()
            return jsonify(activity_guides), 200
        else:
            return jsonify({"error": "Guide not found"}), 404

    except Exception as e:
        print(str(e))
        return jsonify({"error": "Error retrieving activities by guide"}), 500
    

def find_activities_by_place(id):
    try:
        activities = Activity.query.filter_by(place_id=id).all()
        return jsonify([a.json for a in activities]), 200
    except Exception as e: 
        return jsonify({'error': str(e)}), 500


    
