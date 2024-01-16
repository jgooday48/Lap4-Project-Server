from flask import request, Blueprint
from .controller import index, create_note, get_notes_by_notification
from flask_jwt_extended import jwt_required

notes_bp = Blueprint('notes', __name__)


@notes_bp.route("/notes", methods=["POST", "GET"])
def create_notes():
    if request.method == "POST":
        return create_note()
    elif request.method == "GET":
        return index()


@notes_bp.route("/notes/notification/<int:notification_id>", methods=["GET"])
def get_notes(notification_id):
    if request.method == "GET":
        return get_notes_by_notification(notification_id)
