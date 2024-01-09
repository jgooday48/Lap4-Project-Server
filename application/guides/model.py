from application import db
from application.enums import UserType
from werkzeug.security import generate_password_hash, check_password_hash


class Guide(db.Model):
    __tablename__ = "guides"

    tourist_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    user_type = db.Column(db.Enum(UserType), nullable=False)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(), nullable=False)
    password = db.Column(db.Text())
