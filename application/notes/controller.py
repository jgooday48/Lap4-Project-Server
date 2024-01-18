from flask import jsonify, request
from werkzeug import exceptions
from .model import Note
from datetime import datetime
from .. import db


def index():
    note = Note.query.all()
    try:
        return jsonify({"all_note": [m.json for m in note]})
    except:
        raise exceptions.InternalServerError(
            f"Server is down. We are fixing it")


def create_note():
    try:
        data = request.json

        sender_id = data.get('sender_id')
        text = data.get('text')
        guide_id = data.get('guide_id')

        new_note = Note( sender_id=sender_id, text=text, guide_id=guide_id, timestamp = datetime.now() )
        db.session.add(new_note)
        db.session.commit()

        return jsonify(new_note.json), 201

    except Exception as e:
        print(str(e))
        return jsonify({"error": "Error: note cannot be posted"}), 400


def get_notes_by_notification(notification_id):
    try:
        note = Note.query.filter_by(notification_id=notification_id).all()
        return jsonify([m.json for m in note])

    except Exception as e:
        print(str(e))
        return jsonify({"error": "Error: note cannot be retrieved"}), 400


def get_notes_by_guide(guide_id):
    try:
        note = Note.query.filter_by(guide_id=guide_id).all()
        return jsonify([m.json for m in note])

    except Exception as e:
        print(str(e))
        return jsonify({"error": "Error: note cannot be retrieved"}), 400
