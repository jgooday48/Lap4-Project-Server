from flask import request, Blueprint
from werkzeug import exceptions
from .controllers import index, create, show, update, destroy

activities = Blueprint("activities", __name__)

@activities.route('/activities', methods=["GET", "POST"])
def handle_activities():
    if request.method == "POST": return create()
    if request.method == "GET": return index()


@activities.route('/activities/<int:id>', methods=["GET", "PATCH", "DELETE"])
def handle_acivity(id):
    if request.method == "GET": return show(id)
    if request.method == "PATCH": return update(id)
    if request.method == "DELETE": return destroy(id)


@activities.errorhandler(exceptions.NotFound)
def handle_404(err):
    return { "error": f"Oops {err}"}, 404


@activities.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return { "error": f"Oops {err} "}, 500


@activities.errorhandler(exceptions.BadRequest)
def handle_400(err):
    return { "error": f"Oops {err}" }, 400
