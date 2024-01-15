from .extensions import socketio
from flask_socketio import emit
from flask import request

active_users = []

@socketio.on("connect")
def connected():
    emit("connect",{"data": f"id: {request.sid} is connected"})
    print(f"User: {request.sid} has connected")


@socketio.on("new-user-add")
def handle_new_user(new_user_id):
    global active_users
    # If user is not added previously
    if not any(user["userId"] == new_user_id for user in active_users):
        active_users.append({"userId": new_user_id, "socketId": request.sid})
        print("New User Connected", active_users)

    # Send all active users to the new user
    emit("get-users", active_users, broadcast=True)

@socketio.on("disconnect")
def handle_disconnect():
    global active_users

    # Remove user from active users
    active_users = [user for user in active_users if user["socketId"] != request.sid]
    print("User Disconnected", active_users)

    # Send all active users to all users
    emit("get-users", active_users, broadcast=True)

# @socketio.on("join_room")
# def joined(data):
#     username = data['username']
#     room = data['room']
#     emit("message", f'{username} has joined the room {room}')
#     print("message", f'{username} has joined the room {room}')

@socketio.on('data')
def le_message(data):
    print("data from the front end: ",str(data))
    emit("data",{'data':data},broadcast=True)

@socketio.on("send-message")
def handle_send_message(data):
    receiver_id = data["receiverId"]
    sender_id = active_users.get(request.sid)

    if sender_id and receiver_id in active_users.values():
        receiver_socket_id = next((sid for sid, uid in active_users.items() if uid == receiver_id), None)
        if receiver_socket_id:
            emit("recieve-message", data, room=receiver_socket_id)

# @socketio.on("disconnect")
# def disconnected():
#         print("user disconnected")
#         emit("disconnect","user disconnected",broadcast=True)
