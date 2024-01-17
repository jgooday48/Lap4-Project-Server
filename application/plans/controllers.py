from flask import jsonify, request
from werkzeug import exceptions
from .model import Plan
from application.activities.model import Activity

from .. import db

def index(): # GET all plans
    plans = Plan.query.all()
    try:
        return jsonify({"data": [p.json for p in plans]})
    except:
        raise exceptions.InternalServerError(f"Server is down. We are fixing it")

def show(id): #GET a plan
    plan = Plan.query.filter_by(plan_id=id).first()

    try:
        return jsonify({"data": plan.json}), 200
    except:
        raise exceptions.NotFound(f"plan does not exist")
    

def create():
    try:

        tourist_id, guide_id, place_id, date_to, date_from, status, notes, activity_ids = request.json.values()

        new_plan = Plan(tourist_id, guide_id, place_id, date_to,
                        date_from, status, notes)
        print("new plan: ", new_plan)

        existing_activities = Activity.query.filter(
            Activity.activity_id.in_(activity_ids)).all()

        new_plan.activities.extend(existing_activities)

        db.session.add(new_plan)
        db.session.commit()

        return jsonify(new_plan.json), 201
    except Exception as e:
        raise exceptions.BadRequest(f"Failed to post plan: {str(e)}")



def update(id):
    try:
        data = request.json
        plan = Plan.query.filter_by(plan_id=id).first()

        if plan:
            for (attribute, value) in data.items():
                if hasattr(plan, attribute):
                    setattr(plan, attribute, value)

            if "activity_ids" in data:
                activity_ids = data["activity_ids"]
                plan.activities = Activity.query.filter(
                    Activity.activity_id.in_(activity_ids)).all()

            db.session.commit()
            return jsonify(plan.json)
        else:
            raise exceptions.NotFound("Can't find plan")
    except Exception as e:
        print(str(e))  # Print the exception for debugging
        return jsonify({"error": "Internal server error"}), 500




def destroy(id): #DELETE a plan
    try:
        plan = Plan.query.filter_by(plan_id=id).first()
        db.session.delete(plan)
        db.session.commit()
        return "book deleted", 204
    except:
        raise exceptions.NotFound(f"cant find plan")
    

def find_plans_by_guide_id(guide_id):
    try:
        plans = Plan.query.filter_by(guide_id=guide_id).all()

        if plans:
            return jsonify([plan.json for plan in plans])
        else:
            return jsonify({"message": "No plans found for the given guide ID"}), 404
    except Exception as e:
        print(str(e)) 
        return jsonify({"error": "Internal server error"}), 500
    

def find_plans_by_tourist_id(tourist_id):
    try:
        plans = Plan.query.filter_by(tourist_id=tourist_id).all()

        if plans:
            return jsonify([plan.json for plan in plans])
        else:
            return jsonify({"message": "No plans found for the given tourist ID"}), 404
    except Exception as e:
        print(str(e))
        return jsonify({"error": "Internal server error"}), 500
