from application import db
from application.enums import UserType, Filters
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.dialects.postgresql import ARRAY

class Chat(db.Model):
    __tablename__ = "chat"

    chat_id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.Integer)
    receiver = db.Column(db.Integer)

    @property
    def json(self):
        return {
            "chat_id": self.chat_id,
            "sender": self.sender,
            "receiver": self.receiver
        }
