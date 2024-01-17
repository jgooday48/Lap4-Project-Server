from flask import request, Blueprint
from flask_jwt_extended import jwt_required
from .controller import create, userNotification, index, findNotification

notification_bp = Blueprint('notifications', __name__)


@notification_bp.route('/notifications', methods=["POST", "GET"])
def handle_notification():
    if request.method == "POST":
        return create()
    elif request.method == "GET":
        return index()


@notification_bp.route('/notifications/tourist/<int:sender_id>', methods=["GET"])
def find_sender(sender_id):
    if request.method == "GET":
        return userNotification(sender_id)


@notification_bp.route('/notifications/<int:sender_id>/<int:receiver_id>', methods=["GET"])
def find_notification(sender_id, receiver_id):
    if request.method == "GET":
        return findNotification(sender_id, receiver_id)
