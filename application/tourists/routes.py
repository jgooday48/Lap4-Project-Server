from flask import request, Blueprint
from .controller import register, login, find_user
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
