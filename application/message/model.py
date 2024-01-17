from application import db
from application.enums import UserType, Filters
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.dialects.postgresql import ARRAY

class Message(db.Model):
    __tablename__ = "message"

    message_id = db.Column(db.Integer, primary_key=True)
    chat_id = db.Column(db.Integer)
    sender_id = db.Column(db.Integer)
    text = db.Column(db.String(100))
    time = db.Column(db.String(100))

    @property
    def json(self):
        return {
            "message_id": self.message_id,
            "chat_id": self.chat_id,
            "sender_id": self.sender_id,
            "text": self.text,
            "time": self.time
        }
