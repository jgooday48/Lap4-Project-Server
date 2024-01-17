from flask import jsonify, request
from werkzeug import exceptions
from .model import Message

from .. import db

def index():
    message = Message.query.all()
    try:
        return jsonify({"all_message": [m.json for m in message]})
    except:
        raise exceptions.InternalServerError(
            f"Server is down. We are fixing it")
    

def createMessage():
    try:
        data = request.json

        chat_id = data.get('chatId')
        sender_id = data.get('senderId')
        text = data.get('text')
        time = data.get('time')

        new_message = Message(chat_id=chat_id, sender_id=sender_id, text=text, time=time)
        db.session.add(new_message)
        db.session.commit()

        return jsonify(new_message.json), 200
    
    except Exception as e:
        print(str(e))
        return jsonify({"error": "Error: Message cannot be posted"}), 400

def getMessage(chat_id):
    try:
        message = Message.query.filter_by(chat_id=chat_id).all()
        return jsonify([m.json for m in message])
    
    except Exception as e:
        print(str(e))
        return jsonify({"error": "Error: Message cannot be retrieved"}), 400
