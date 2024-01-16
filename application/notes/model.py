from application import db
from application.enums import UserType, Filters
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.dialects.postgresql import ARRAY


class Note(db.Model):
    __tablename__ = "notes"

    note_id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer)
    text = db.Column(db.String(100))
    guide_id = db.Column(db.Integer, db.ForeignKey('guides.guide_id'))
    timestamp = db.Column(db.DateTime())


    @property
    def json(self):
        return {
            "note_id": self.note_id,
            "sender_id": self.sender_id,
            "text": self.text,
            "guide_id": self.guide_id,
            "timestamp": self.timestamp
        }
