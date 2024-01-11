from flask import request, Blueprint
from werkzeug import exceptions
from .controllers import index, create, show, update

places_bp = Blueprint("places", __name__)

@places_bp.route('/places', methods=["GET", "POST"])
def handle_places():
    if request.method == "POST": return create()
    if request.method == "GET": return index()


@places_bp.route('/places/<int:id>', methods=["GET", "PATCH"])
def handle_place(id):
    if request.method == "GET": return show(id)
    if request.method == "PATCH": return update(id)



@places_bp.errorhandler(exceptions.NotFound)
def handle_404(err):
    return { "error": f"Oops {err}"}, 404


@places_bp.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return { "error": f"Oops {err} "}, 500


@places_bp.errorhandler(exceptions.BadRequest)
def handle_400(err):
    return { "error": f"Oops {err}" }, 400
