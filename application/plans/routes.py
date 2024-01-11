from flask import request, Blueprint
from werkzeug import exceptions
from .controllers import index, create, show, update, destroy

plans_bp = Blueprint("plans", __name__)

@plans_bp.route('/plans', methods=["GET", "POST"])
def handle_activities():
    if request.method == "POST": return create()
    if request.method == "GET": return index()


@plans_bp.route('/plans/<int:id>', methods=["GET", "PATCH", "DELETE"])
def handle_acivity(id):
    if request.method == "GET": return show(id)
    if request.method == "PATCH": return update(id)
    if request.method == "DELETE": return destroy(id)


@plans_bp.errorhandler(exceptions.NotFound)
def handle_404(err):
    return { "error": f"Oops {err}"}, 404


@plans_bp.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return { "error": f"Oops {err} "}, 500


@plans_bp.errorhandler(exceptions.BadRequest)
def handle_400(err):
    return { "error": f"Oops {err}" }, 400
