from .extensions import socketio
from flask_socketio import emit
from flask import request

@socketio.on("connect")
def connected():
    print(request.sid)
    emit("connect",{"data": "id is connected"})
    print("client has connected")

@socketio.on('data')
def le_message(data):
    print("data from the front end: ",str(data))
    emit("data",{'data':data},broadcast=True)

@socketio.on("disconnect")
def disconnected():
        print("user disconnected")
        emit("disconnect","user disconnected",broadcast=True)
