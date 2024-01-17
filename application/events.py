from .extensions import socketio
from flask_socketio import emit
from flask import request
from datetime import datetime


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
        emit("get-users", active_users)

    # Handle message sending
@socketio.on("send-message")
def handle_send_message(data):
    try:
        receiver_id = data["receiverId"]
        # sender_id = active_users.get(request.sid, {}).get("userId")

        # if sender_id and any(user.get("userId") == receiver_id for user in active_users.values()):
        #     receiver_socket_id = next((sid for sid, user in active_users.items() if user.get("userId") == receiver_id), None)
        #     if receiver_socket_id:
        emit("recieve-message", receiver_id)
        print("success", receiver_id)

    except Exception as e:
        print(f"Error in handle_send_message: {str(e)}")

    # Handle disconnection
@socketio.on("disconnect")
def handle_disconnect():
        global active_users
        # Remove user from active users
        active_users.pop(request.sid, None)
        print("User Disconnected", active_users)
        # Send all active users to all users
        emit("get-users", active_users, broadcast=True)




@socketio.on('notification')
def handle_notification(data):
    from application import db  # Import locally
    from application.notes.model import Note  # Import locally
    
    # Handle the notification data (store it in the database)
    guide_id = data.get('guideId')
    message = data.get('message')
    sender_id = data.get('senderId')


    new_note = Note( sender_id=sender_id,text=message,guide_id=guide_id, timestamp=datetime.now())
        # Add the note to the database
    db.session.add(new_note)
    db.session.commit()

        # Emit a response to acknowledge the notification
    emit('notification_ack', { 'status': 'success'}, room=request.sid)
    emit('notification', {'message': message, 'senderId': sender_id,'timestamp': new_note.timestamp}, room=guide_id)


