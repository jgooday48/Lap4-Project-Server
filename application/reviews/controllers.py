from flask import jsonify, request
from werkzeug import exceptions
from .model import Review

from .. import db

def index(): # GET all reviews
    reviews = Review.query.all()

    try:
        return jsonify({"data": [r.json for r in reviews]})
    except:
        raise exceptions.InternalServerError(f"Server is down. We are fixing it")

def show(id): #GET a review
    review = Review.query.filter_by(review_id=id).first()

    try:
        return jsonify({"data": review.json}), 200
    except:
        raise exceptions.NotFound(f"review does not exist")
    
def create(): #POST a review
    try:
        guide_id,tourist_id, rating, comment = request.json.values()
        new_review = Review(guide_id,tourist_id, rating, comment)
        db.session.add(new_review)
        db.session.commit()
        return jsonify({ "data": new_review.json}), 201
    except:
        raise exceptions.BadRequest(f"cant post review")


def update(id): #PATCH a review
    try:
        data = request.json
        review = Review.query.filter_by(review_id=id).first()

        for (attribute, value) in data.items():
            if hasattr(review, attribute):
                setattr(review, attribute, value)
        db.session.commit()
        return jsonify({ "data":review.json})
    except:
        raise exceptions.NotFound(f"cant post review")

def destroy(id): #DELETE a review
    try:
        review = Review.query.filter_by(review_id=id).first()
        db.session.delete(review)
        db.session.commit()
        return "book deleted", 204
    except:
        raise exceptions.NotFound(f"cant post review")
