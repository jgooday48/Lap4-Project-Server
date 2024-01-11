# from application import app
from flask import jsonify, Blueprint

main_bp = Blueprint("main", __name__)


@main_bp.route('/')
def hello():
    return jsonify({
        "message": "Welcome",
        "description": "",
        "endpoints": [
            "GET /"
        ]
    }), 200
