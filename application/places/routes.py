from flask import request, Blueprint
from werkzeug import exceptions
from .controllers import index, create, show, update, destroy

places = Blueprint("places", __name__)

@places.route('/places', methods=["GET", "POST"])
def handle_places():
    if request.method == "POST": return create()
    if request.method == "GET": return index()


@places.route('/places/<int:id>', methods=["GET", "PATCH", "DELETE"])
def handle_place(id):
    if request.method == "GET": return show(id)
    if request.method == "PATCH": return update(id)
    if request.method == "DELETE": return destroy(id)


@places.errorhandler(exceptions.NotFound)
def handle_404(err):
    return { "error": f"Oops {err}"}, 404


@places.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return { "error": f"Oops {err} "}, 500


@places.errorhandler(exceptions.BadRequest)
def handle_400(err):
    return { "error": f"Oops {err}" }, 400
