from application import db
from application.enums import UserType, Filters
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.dialects.postgresql import ARRAY

class Notification(db.Model):
    __tablename__ = "chat"

    notice_id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.Integer)
    receiver = db.Column(db.Integer)

    @property
    def json(self):
        return {
            "notice_id": self.notice_id,
            "sender": self.sender,
            "receiver": self.receiver
        }
