from flask import jsonify, request
from werkzeug import exceptions
from .model import Activity
from application.enums import Specialisation
from .. import db

def index(): # GET all activities
    activities = Activity.query.all()

    try:
        return jsonify({"data": [a.json for a in activities]})
    except:
        raise exceptions.InternalServerError(f"Server is down. We are fixing it")

def show(id): #GET a activity
    activity = Activity.query.filter_by(activity_id=id).first()

    try:
        return jsonify({"data": activity.json}), 200
    except:
        raise exceptions.NotFound(f"activity does not exist")
    
def create(): #POST an activity
    try:
        name, location, specialisation, place_id, description, post_code = request.json.values()

        new_activity= Activity(name, location, specialisation, place_id, description, post_code)
        db.session.add(new_activity)
        db.session.commit()
        return jsonify({ "data": new_activity.json}), 201
    except:
        raise exceptions.BadRequest(f"cant post activity")


def update(id): #PATCH an activity
    try:
        data = request.json
        activity = Activity.query.filter_by(activity_id=id).first()

        for (attribute, value) in data.items():
            if hasattr(activity, attribute):
                setattr(activity, attribute, value)
        db.session.commit()
        return jsonify({ "data":activity.json})
    except:
        raise exceptions.NotFound(f"place does not exist")

def destroy(id): #DELETE an activity
    try:
        activity = Activity.query.filter_by(activity_id=id).first()
        db.session.delete(activity)
        db.session.commit()
        return "activity deleted", 204
    except:
        raise exceptions.NotFound(f"place does not exist")