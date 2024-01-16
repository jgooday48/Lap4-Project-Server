from .extensions import socketio
from flask_socketio import emit
from flask import request

active_users = {}

@socketio.on("connect")
def handle_connect():
    print(f"User connected: {request.sid}")

    # Handle new user addition
    @socketio.on("new-user-add")
    def handle_new_user(new_user_id):
        global active_users
        if request.sid not in active_users:
            active_users[request.sid] = {"userId": new_user_id, "socketId": request.sid}
            print("New User Connected", active_users)
        # Send all active users to the new user
        emit("get-users", active_users, broadcast=True, include_self=False)

    # Handle message sending
    @socketio.on("send-message")
    def handle_send_message(data):
        receiver_id = data["receiverId"]
        sender_id = active_users.get(request.sid)

        if sender_id and receiver_id in active_users.values():
            receiver_socket_id = next((sid for sid, uid in active_users.items() if uid == receiver_id), None)
            if receiver_socket_id:
                emit("recieve-message", data, room=receiver_socket_id)

    # Handle disconnection
    @socketio.on("disconnect")
    def handle_disconnect():
        global active_users
        # Remove user from active users
        active_users = {sid: user for sid, user in active_users.items() if sid != request.sid}
        print("User Disconnected", active_users)
        # Send all active users to all users
        emit("get-users", active_users, broadcast=True)

# @socketio.on("connect")
# def connected():
#     emit("connect",{"data": f"id: {request.sid} is connected"})
#     print(f"User: {request.sid} has connected")


# @socketio.on("new-user-add")
# def handle_new_user(new_user_id):
#     global active_users
#     if request.sid not in active_users:
#         active_users[request.sid] = {"userId": new_user_id, "socketId": request.sid}
#         print("New User Connected", active_users)
#     # Send all active users to the new user
#         emit("get-users", active_users, broadcast=True, include_self=False)

# @socketio.on("disconnect")
# def handle_disconnect():
#     global active_users
#     # Remove user from active users
#     del active_users[request.sid]
#     print("User Disconnected", active_users)
#     # Send all active users to all users
#     emit("get-users", active_users, broadcast=True, include_self=False)

# # @socketio.on("join_room")
# # def joined(data):
# #     username = data['username']
# #     room = data['room']
# #     emit("message", f'{username} has joined the room {room}')
# #     print("message", f'{username} has joined the room {room}')

# @socketio.on('data')
# def le_message(data):
#     print("data from the front end: ",str(data))
#     emit("data",{'data':data},broadcast=True)

# @socketio.on("send-message")
# def handle_send_message(data):
#     receiver_id = data["receiverId"]
#     sender_id = active_users.get(request.sid, {}).get("userId")

#     if sender_id and receiver_id in [user.get("userId") for user in active_users.values()]:
#         receiver_socket_id = next((sid for sid, user in active_users.items() if user.get("userId") == receiver_id), None)
#         if receiver_socket_id:
#             emit("recieve-message", data, room=receiver_socket_id)

# @socketio.on("disconnect")
# def disconnected():
#         print("user disconnected")
#         emit("disconnect","user disconnected",broadcast=True)
