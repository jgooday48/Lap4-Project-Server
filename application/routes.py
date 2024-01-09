# from application import app
from flask import jsonify, Blueprint

main = Blueprint("main", __name__)


@main.route('/')
def hello():
    return jsonify({
        "message": "Welcome",
        "description": "",
        "endpoints": [
            "GET /"
        ]
    }), 200
