from flask import Blueprint, jsonify
from flask_jwt_extended import get_jwt, jwt_required
from .model import Token

token_bp = Blueprint("tokens",__name__)



@token_bp.get("/logout")
@jwt_required(verify_type=False)
def logoout():
    jwt = get_jwt()

    jti = jwt['jti']
    token_type = jwt['type']
    token = Token(jti=jti)
    token.save()

    return jsonify({"message": f"Logout Successful! {token_type} has been revoked sucessfully"})

