from flask import request, Blueprint

from .controller import register, login, find_user_by_email,find_user_by_username, current_tourist, refresh_access, find_guides_by_tourist, join_tourist_and_guide, remove_tourist_guide_pair, index, find_user_id
from flask_jwt_extended import jwt_required


tourist_bp = Blueprint('tourists', __name__)

@tourist_bp.route('/tourists', methods=["GET"])
def handle_tourists():
    if request.method == "GET": return index()

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
      return find_user_by_username(username)
   

@tourist_bp.route("/tourists/email/<email>", methods=['GET'])
# @jwt_required()
def handle_email(email): 
   if request.method == 'GET': 
      return find_user_by_email(email)

   
@tourist_bp.route("/tourist/<int:id>", methods=['GET'])
def find_tourist(id):
   if request.method == 'GET':
      return find_user_id(id)
   
@tourist_bp.route("/tourists/<id>/guides", methods=["GET"])
def handle_get_guides_by_tourist(id): 
   if request.method == 'GET': return find_guides_by_tourist(id)


@tourist_bp.route("/tourists/current", methods=['GET'])
@jwt_required()
def handle_current_user():
   if request.method == 'GET':
      return current_tourist()
   

@tourist_bp.route("/tourists/refresh", methods=['GET'])
@jwt_required(refresh=True)
def handle_refresh_token():
   return refresh_access()


@tourist_bp.route("/tourists/guides", methods=['POST'])
def handle_pair_tourist_guide(): 
   return join_tourist_and_guide()


@tourist_bp.route("/tourists/guides/<tourist_id>/<guide_id>", methods=['DELETE'])
def handle_remove_tourist_guide_pair(tourist_id, guide_id):
   return remove_tourist_guide_pair(tourist_id, guide_id)
