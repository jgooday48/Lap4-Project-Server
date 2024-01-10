from application import db
from application.enums import Filters
from sqlalchemy.dialects.postgresql import ARRAY
from application.guides import model





class Activity(db.Model):
    __tablename__ = "activities"

    activity_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    location = db.Column(db.String(200), nullable=False)
    filters = db.Column(ARRAY(db.Enum(Filters)))
    place_id = db.Column(db.Integer, db.ForeignKey('places.place_id'))
    description = db.Column(db.String(), nullable=False)
    zip_code = db.Column(db.String(100), nullable=False)
  
    @property
    def json(self):
        return {
            "activity_id": self.activity_id,
            "name": self.name,
            "location": self.location,
            "filters": [f.value for f in self.filters],
            "place_id": self.place_id,
            "description": self.description,
            "zip_code": self.zip_code
        }
    
    def get_guides(self):
        return [guide.json for guide in self.guides]
