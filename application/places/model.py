from application import db
from sqlalchemy.dialects.postgresql import ARRAY


class Place(db.Model):
    __tablename__ = "places"

    place_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    location = db.Column(db.String(150), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    tags = db.Column(ARRAY(db.String(150)), nullable=False)
    images=db.Column(ARRAY(db.String()), nullable=True)
    # google_api = db.Column(db.String(150), nullable=False)
    activities = db.relationship('Activity', backref='place', lazy=True, foreign_keys='Activity.place_id')
    plans = db.relationship('Guide', backref='place', lazy=True, foreign_keys='Guide.place_id')



    def __init__(self, name, location, description, tags, images):
        self.name = name
        self.location = location
        self.description = description
        self.tags = tags
        self.images = images
        # self.google_api = google_api
    

    @property
    def json(self):
        return {
            "place_id": self.place_id,
            "name": self.name,
            "location": self.location,
            "description": self.description,
            "tags": self.tags,
            "images": self.images
            
            # "google_api": self.google_api
        }

