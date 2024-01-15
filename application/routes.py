from flask import jsonify, Blueprint

main_bp = Blueprint("main", __name__)


@main_bp.route('/')
def hello():
    return jsonify({
        "message": "Welcome",
        "description": "",
        "endpoints": [
            "GET /"
            "/places"
            "/activities"
            "/guides"
            "/plans"
            "/reviews"
        ]
    }), 200
