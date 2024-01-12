from application import db
from datetime import datetime
from application.enums import Status

class Plan(db.Model):
    __tablename__ = "plans"

    plan_id = db.Column(db.Integer, primary_key=True)
    tourist_id = db.Column(db.Integer, db.ForeignKey('tourists.tourist_id'), nullable=False)
    guide_id = db.Column(db.Integer, db.ForeignKey('guides.guide_id'), nullable=False)
    date_from = db.Column(db.DateTime, nullable=False, default=datetime.now())
    date_to = db.Column(db.DateTime, nullable=False, default=datetime.now())
    activity_id = db.Column(db.Integer, db.ForeignKey('activities.activity_id'), nullable=False)
    status = db.Column(db.Enum(Status), nullable=False)

    def __init__(self, tourist_id, guide_id, date_from, date_to, activity_id, status):
        self.tourist_id = tourist_id
        self.guide_id = guide_id
        self.date_to: date_to
        self.date_from = date_from
        self.activity_id= activity_id
        self.status = status


    @property
    def json(self):
        return {
            "plan_id": self.plan_id,
            "tourist_id": self.tourist_id,
            "guide_id": self.guide_id,
            "date_from": self.date_from,
            "date_to": self.date_to,
            "activity_id": self.activity_id,
            "status": self.status.value
        }
