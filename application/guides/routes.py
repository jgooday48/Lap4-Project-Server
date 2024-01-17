from flask import request, Blueprint
from flask_jwt_extended import jwt_required

from .controller import register, login, find_user_by_email, find_user_by_username, refresh_access, current_guide, find_activities_by_guide, index, add_activity_to_guide, guides_by_place_id, find_guide_by_index, update



guide_bp = Blueprint('guides', __name__)


@guide_bp.route('/guides', methods=["GET"])
def handle_guides():
    if request.method == "GET": return index()

@guide_bp.route('/guides/<int:id>', methods=["GET", "PATCH"])
def handle_guide(id):
    if request.method == "GET": return find_guide_by_index(id)
    if request.method == "PATCH": return update(id)


@guide_bp.route('/guides/register', methods=['POST'])
def handle_user_register():
   if request.method == 'POST':
      return register()

@guide_bp.route('/guides/login', methods=['POST'])
def handle_user_login():
   if request.method == 'POST':
      return login()
   

@guide_bp.route('/guides/activities', methods=['POST'])
def handle_activity_guide_pair():
   if request.method == 'POST': 
      return add_activity_to_guide()


@guide_bp.route("/guides/email/<email>", methods=['GET'])
# @jwt_required()
def handle_email(email):
   if request.method == 'GET': return find_user_by_email(email)


@guide_bp.route("/guides/username/<username>", methods=['GET'])
# @jwt_required()
def handle_username(username):
   if request.method == 'GET': return find_user_by_username(username)

@guide_bp.route("/guides/guideId:<id>/activities", methods=['GET'])
def handle_activities_by_guide(id):
   if request.method == 'GET': return find_activities_by_guide(id)
   

@guide_bp.route("/guides/current", methods=['GET'])
@jwt_required()
def handle_current_user():
   if request.method == 'GET':
      return current_guide()



@guide_bp.route("/guides/refresh", methods=['GET'])
@jwt_required(refresh=True)
def handle_refresh_token():
   return refresh_access()


@guide_bp.route("/guides/placeId:<id>", methods=['GET'])
def handle_guides_by_place_id(id): 
   return guides_by_place_id(id)
