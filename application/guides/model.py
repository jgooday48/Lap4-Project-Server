from application import db
from application.enums import UserType, Filters
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.dialects.postgresql import ARRAY


guide_activity = db.Table('guide_activity',
                          db.Column('guide_id', db.Integer,
                                    db.ForeignKey('guides.guide_id')),
                          db.Column('activity_id', db.Integer,
                                    db.ForeignKey('activities.activity_id'))
)
                          

class Guide(db.Model):
    __tablename__ = "guides"

    guide_id = db.Column(db.Integer, primary_key=True)
    place_id = db.Column(db.Integer, db.ForeignKey('places.place_id'))
    name = db.Column(db.String(100), nullable=False)
    tagline = db.Column(db.String())
    user_type = db.Column(db.Enum(UserType), nullable=False)
    username = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(), nullable=False)
    password = db.Column(db.Text())
    filters = db.Column(ARRAY(db.Enum(Filters)))
    activities = db.relationship(
        'Activity', secondary=guide_activity, backref=db.backref('guides', lazy='dynamic')
    )
    plans = db.relationship('Plan', backref='guide', lazy=True, foreign_keys='Plan.guide_id')
    reviews = db.relationship('Review', backref='guide', lazy=True, foreign_keys='Review.guide_id')
    availible_from = db.Column(db.DateTime, nullable=False)
    availible_to = db.Column(db.DateTime, nullable=False)
    info = db.Column(db.String())
    images=db.Column(ARRAY(db.String()), nullable=True)



    # def __repr__(self):
    #     return f"<Guide: {self.username}"

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def get_activities(self):
        return [activity.json for activity in self.activities]
    
    def add_activity(self, activity):
        if activity not in self.activities:
            self.activities.append(activity)
            db.session.commit()

    @classmethod
    def get_user_by_username(cls, username):
        return cls.query.filter_by(username=username).first()
    
    @classmethod
    def get_user_by_email(cls, email):
        return cls.query.filter_by(email=email).first()
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.add(self)
        db.session.commit()

    @property
    def json(self):
        return {
            "guide_id": self.guide_id,
            "place_id":self.place_id,
            "name": self.name,
            "tagline": self.tagline,
            "user_type": self.user_type.value,
            "username": self.username,
            "email": self.email,
            "password": self.password,
            "filters": [f.value for f in self.filters],
            "availible_from": self.availible_from,
            "availible_to": self.availible_to,
            "info": self.info,
            "images":self.images,
        }

