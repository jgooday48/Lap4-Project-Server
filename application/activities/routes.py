from flask import Blueprint, request
from .controllers import index, show, create, update, destroy, find_guides_by_activity


activities_bp = Blueprint("activities",__name__)


@activities_bp.route('/activities', methods=["GET", "POST"])
def handle_activities():
    if request.method == "GET": return index()
    if request.method == 'POST': return create()


@activities_bp.route('/activities/<int:id>', methods=["GET", "PATCH", "DELETE"])
def handle_activity(id):
    if request.method == "GET": return show(id)
    if request.method == "PATCH": return update(id)
    if request.method == "DELETE": return destroy(id)
    

@activities_bp.route('/activities/<int:id>/guides', methods=["GET"])
def handle_activity_guides(id):
    if request.method == "GET": return find_guides_by_activity(id)
