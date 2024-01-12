from flask import jsonify, request
from werkzeug import exceptions
from .model import Place

from .. import db

def index(): # GET all places
    places = Place.query.all()

    try:
        return jsonify({"data": [p.json for p in places]})
    except:
        raise exceptions.InternalServerError(f"Server is down. We are fixing it")

def show(id): #GET a place ded
    place = Place.query.filter_by(place_id=id).first()

    try:
        return jsonify({"data": place.json}), 200
    except:
        raise exceptions.NotFound(f"place does not exist")
    
def create(): #POST a place
    try:
        name, location, description, tags, images = request.json.values()
        new_place = Place(name, location, description, tags, images)
        db.session.add(new_place)
        db.session.commit()
        return jsonify({ "data": new_place.json}), 201
    except:
        raise exceptions.BadRequest(f"cant post place")


def update(id): #PATCH a place
    try:
        data = request.json
        place = Place.query.filter_by(place_id=id).first()

        for (attribute, value) in data.items():
            if hasattr(place, attribute):
                setattr(place, attribute, value)
        db.session.commit()
        return jsonify({ "data":place.json})
    except:
        raise exceptions.NotFound(f"place does not exist")
def destroy(id): #DELETE a place
    try:
        place = Place.query.filter_by(place_id=id).first()
        db.session.delete(place)
        db.session.commit()
    except:
        raise exceptions.NotFound(f"place does not exist")






