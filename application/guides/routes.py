from flask import request, Blueprint
from flask_jwt_extended import jwt_required
from .controller import register, login, find_user, refresh_access, current_guide, find_activities_by_guide, index


guide_bp = Blueprint('guides', __name__)


@guide_bp.route('/guides', methods=["GET"])
def handle_guides():
    if request.method == "GET": return index()



@guide_bp.route('/guides/register', methods=['POST'])
def handle_user_register():
   if request.method == 'POST':
      return register()


@guide_bp.route('/guides/login', methods=['POST'])
def handle_user_login():
   if request.method == 'POST':
      return login()


@guide_bp.route("/guides/username/<username>", methods=['GET'])
# @jwt_required()
def handle_username(username):
   if request.method == 'GET': return find_user(username)

@guide_bp.route("/guides/username/<username>/activities", methods=['GET'])
def handle_activities_by_guide(username):
   if request.method == 'GET': return find_activities_by_guide(username)
   

@guide_bp.route("/guides/current", methods=['GET'])
@jwt_required()
def handle_current_user():
   if request.method == 'GET':
      return current_guide()



@guide_bp.route("/guides/refresh", methods=['GET'])
@jwt_required(refresh=True)
def handle_refresh_token():
   return refresh_access()
