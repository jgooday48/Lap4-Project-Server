from flask import request, Blueprint
from werkzeug import exceptions
from .controllers import index, create, show, update, destroy

reviews_bp = Blueprint("reviews", __name__)

@reviews_bp.route('/reviews', methods=["GET", "POST"])
def handle_activities():
    if request.method == "POST": return create()
    if request.method == "GET": return index()


@reviews_bp.route('/reviews/<int:id>', methods=["GET", "PATCH", "DELETE"])
def handle_acivity(id):
    if request.method == "GET": return show(id)
    if request.method == "PATCH": return update(id)
    if request.method == "DELETE": return destroy(id)


@reviews_bp.errorhandler(exceptions.NotFound)
def handle_404(err):
    return { "error": f"Oops {err}"}, 404


@reviews_bp.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return { "error": f"Oops {err} "}, 500


@reviews_bp.errorhandler(exceptions.BadRequest)
def handle_400(err):
    return { "error": f"Oops {err}" }, 400
