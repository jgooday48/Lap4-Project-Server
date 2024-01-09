from flask import jsonify, request
from werkzeug import exceptions
from .model import Place

from .. import db

def index():
    places = Place.query.all()

    try:
        return jsonify({"data": [p.json for p in places]})
    except:
        raise exceptions.InternalServerError(f"Server is down. We are fixing it")
