from flask import jsonify, request
from werkzeug import exceptions
from .model import Chat
from sqlalchemy import func

from .. import db

def index():
    chat = Chat.query.all()
    try:
        return jsonify({"all_chats": [c.json for c in chat]})
    except:
        raise exceptions.InternalServerError(
            f"Server is down. We are fixing it")


def create():
    try:
        data = request.json

        sender_id = data.get('senderId')
        receiver_id = data.get('receiverId')

        new_chat = Chat(sender=sender_id, receiver=receiver_id)
        
        db.session.add(new_chat)
        db.session.commit()

        return jsonify(new_chat.json), 200
    
    except Exception as e:
        print(str(e))
        return jsonify({"error": "Error: Chat cannot be posted"}), 400

def userChat(sender_id):
    try:
        chats = Chat.query.filter_by(sender=sender_id)
        return jsonify([chat.json for chat in chats]), 200
    
    except Exception as e:
        print(str(e))
        return jsonify({"error": "Error: Chat cannot be retrieved"}), 400
    
def guideChat(receiver_id):
    try:
        chats = Chat.query.filter_by(receiver=receiver_id)
        return jsonify([chat.json for chat in chats]), 200
    
    except Exception as e:
        print(str(e))
        return jsonify({"error": "Error: Chat cannot be retrieved"}), 400

def findChat(sender_id, receiver_id):
    try:
        chat = Chat.query.filter_by(sender=sender_id, receiver=receiver_id).first()
        return jsonify(chat.json), 200
    except Exception as e:
        print(str(e))
        return jsonify({"error": "Error: Chat cannot be retrieved"}), 400
