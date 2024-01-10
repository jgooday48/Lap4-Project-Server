from flask import jsonify, request
from werkzeug import exceptions
from .model import Activity

from .. import db


def index(): 
    activities = Activity.query.all()

    try:
        return jsonify({"all activities": [a.json for a in activities]})
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


        new_activity = Activity(
            name=name,
            location=location,
            filters=filters,
            place_id=place_id,
            description=description,
            zip_code=zip_code
        )

        db.session.add(new_activity)
        db.session.commit()

        return jsonify(new_activity.json), 201

    except Exception as e:
        print(str(e))
        return jsonify({"error": "Error: Activity cannot be posted"}), 400


def update(id):
    data = request.json
    activity = Activity.query.filter_by(activity_id=id).first()

    for (attribute, value) in data.items():
        if hasattr(activity, attribute):
            setattr(activity, attribute, value)

    db.session.commit()
    return jsonify({"updated activity": activity.json})


def destroy(id):
    activity = Activity.query.filter_by(activity_id=id).first()
    db.session.delete(activity)
    db.session.commit()
    return "Activity Deleted", 204


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

