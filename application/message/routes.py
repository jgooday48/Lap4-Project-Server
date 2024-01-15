from flask import request, Blueprint
from .controller import index, createMessage, getMessage
from flask_jwt_extended import jwt_required

message_bp = Blueprint('message', __name__)

@message_bp.route("/message", methods=["POST", "GET"])
def create_message():
    if request.method == "POST":
        return createMessage()
    elif request.method == "GET":
        return index()
    
@message_bp.route("/message/<int:chat_id>", methods=["GET"])
def get_message(chat_id):
    if request.method == "GET":
        return getMessage(chat_id)
