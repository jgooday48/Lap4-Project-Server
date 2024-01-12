from .extensions import socketio
from flask_socketio import emit
from flask import request

@socketio.on("connect")
def connected():
    emit("connect",{"data": f"id: {request.sid} is connected"})
    print(f"User: {request.sid} has connected")

@socketio.on("join_room")
def joined(data):
    username = data['username']
    room = data['room']
    emit("message", f'{username} has joined the room {room}')
    print("message", f'{username} has joined the room {room}')

@socketio.on('data')
def le_message(data):
    print("data from the front end: ",str(data))
    emit("data",{'data':data},broadcast=True)

@socketio.on("disconnect")
def disconnected():
        print("user disconnected")
        emit("disconnect","user disconnected",broadcast=True)
