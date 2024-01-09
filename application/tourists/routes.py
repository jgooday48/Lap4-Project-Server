from flask import request, Blueprint
from .controller import register, login, find_user, current_tourist, refresh_access
from flask_jwt_extended import jwt_required


tourist_bp = Blueprint('tourists', __name__)


@tourist_bp.route('/tourists/register', methods=['POST'])
def handle_user_register():
   if request.method == 'POST':
      return register()
   

@tourist_bp.route('/tourists/login', methods=['POST'])
def handle_user_login():
   if request.method == 'POST':
      return login()
   
@tourist_bp.route("/tourists/username/<username>", methods=['GET'])
# @jwt_required()
def handle_username(username): 
   if request.method == 'GET': 
      return find_user(username)


@tourist_bp.route("/tourists/current", methods=['GET'])
@jwt_required()
def handle_current_user():
   if request.method == 'GET':
      return current_tourist()
   

@tourist_bp.route("/tourists/refresh", methods=['GET'])
@jwt_required(refresh=True)
def handle_refresh_token():
   return refresh_access()


