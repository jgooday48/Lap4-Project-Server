from application import db
from datetime import datetime
from application.enums import Status


plans_activities_association = db.Table(
    'plans_activities_association',
    db.Model.metadata,
    db.Column('plan_id', db.Integer, db.ForeignKey('plans.plan_id')),
    db.Column('activity_id', db.Integer,
    db.ForeignKey('activities.activity_id'))
)

class Plan(db.Model):
    __tablename__ = "plans"

    plan_id = db.Column(db.Integer, primary_key=True)
    tourist_id = db.Column(db.Integer, db.ForeignKey('tourists.tourist_id'), nullable=False)
    guide_id = db.Column(db.Integer, db.ForeignKey('guides.guide_id'), nullable=False)
    place_id = db.Column(db.Integer, db.ForeignKey('places.place_id'))
    date_from = db.Column(db.DateTime, nullable=False, default=datetime.now())
    date_to = db.Column(db.DateTime, nullable=False, default=datetime.now())
    activities = db.relationship('Activity', secondary=plans_activities_association, backref='plans', lazy='dynamic')
    notes = db.Column(db.String(), nullable=True)
    status = db.Column(db.Enum(Status), nullable=False)

    # place = db.relationship('Place', backref='plans', foreign_keys=[place_id])

    def __init__(self, tourist_id, guide_id, place_id, date_from, date_to, status, notes):
        self.tourist_id = tourist_id
        self.guide_id = guide_id
        self.place_id = place_id
        self.date_to = date_to
        self.date_from = date_from
        self.status = status
        self.notes = notes
        
    @property
    def json(self):
        return {
            "plan_id": self.plan_id,
            "tourist_id": self.tourist_id,
            "guide_id": self.guide_id,
            "place_id": self.place_id,
            "date_from": self.date_from.strftime("%Y-%m-%d %H:%M:%S"),
            "date_to": self.date_to.strftime("%Y-%m-%d %H:%M:%S"),
            "activities": [{"activity_id": activity.activity_id} for activity in self.activities],
            "status": self.status.value,
            "notes": self.notes
        }

