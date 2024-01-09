# from flask import jsonify, request
# from werkzeug import exceptions
# from .model import Plan

# from .. import db

# def index(): # GET all plans
#     plans = Plan.query.all()

#     try:
#         return jsonify({"data": [p.json for p in plans]})
#     except:
#         raise exceptions.InternalServerError(f"Server is down. We are fixing it")

# def show(id): #GET a plan
#     plan = Plan.query.filter_by(plan_id=id).first()

#     try:
#         return jsonify({"data": plan.json}), 200
#     except:
#         raise exceptions.NotFound(f"plan does not exist")
    
# def create(): #POST a plan
#     try:
#         tourist_id, guide_id, timestamp, activity_id = request.json.values()
#         new_plan = Plan(tourist_id, guide_id, timestamp, activity_id)
#         db.session.add(new_plan)
#         db.session.commit()
#         return jsonify({ "data": new_plan.json}), 201
#     except:
#         raise exceptions.BadRequest(f"cant post plan")


# def update(id): #PATCH a plan
#     data = request.json
#     plan = Plan.query.filter_by(plan_id=id).first()

#     for (attribute, value) in data.items():
#         if hasattr(plan, attribute):
#             setattr(plan, attribute, value)
#     db.session.commit()
#     return jsonify({ "data":plan.json})

# def destroy(id): #DELETE a plan
#     plan = Plan.query.filter_by(plan_id=id).first()
#     db.session.delete(plan)
#     db.session.commit()
#     return "book deleted", 204
