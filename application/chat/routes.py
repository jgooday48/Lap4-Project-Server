from flask import request, Blueprint
from flask_jwt_extended import jwt_required
from .controller import create, userChat, index, findChat

chat_bp = Blueprint('chat', __name__)


@chat_bp.route('/chat', methods=["POST", "GET"])
def handle_chat():
    if request.method == "POST":
        return create()
    elif request.method == "GET":
        return index()

@chat_bp.route('/chat/<int:sender_id>', methods=["GET"])
def find_sender(sender_id):
    if request.method == "GET":
        return userChat(sender_id)
    
@chat_bp.route('/chat/<int:sender_id>/<int:receiver_id>', methods=["GET"])
def find_chat(sender_id, receiver_id):
    if request.method == "GET":
        return findChat(sender_id, receiver_id)
