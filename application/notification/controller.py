from flask import jsonify, request
from werkzeug import exceptions
from .model import Notification
from sqlalchemy import func

from .. import db


def index():
    notifications = Notification.query.all()
    try:
        return jsonify({"all_notifications": [n.json for n in notifications]})
    except:
        raise exceptions.InternalServerError(
            f"Server is down. We are fixing it")
    

def create():
    try:
        data = request.json

        sender_id = data.get('sender')
        receiver_id = data.get('receiver')

        new_notification = Notification(sender=sender_id, receiver=receiver_id)
    

        db.session.add(new_notification)
        db.session.commit()

        return jsonify(new_notification.json), 201

    except Exception as e:
        print(str(e))
        return jsonify({"error": "Error: notification cannot be posted"}), 400
    

def userNotification(sender_id):
    try:
        notifications = Notification.query.filter_by(sender=sender_id)
        return jsonify([notification.json for notification in notifications]), 200

    except Exception as e:
        print(str(e))
        return jsonify({"error": "Error: notification cannot be retrieved"}), 400
    

def findNotification(sender_id, receiver_id):
    try:
        notification = Notification.query.filter_by(
            sender=sender_id, receiver=receiver_id).first()
        return jsonify(notification.json), 200
    except Exception as e:
        print(str(e))
        return jsonify({"error": "Error: notification cannot be retrieved"}), 400

    


    

