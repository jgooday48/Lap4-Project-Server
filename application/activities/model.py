from application import db
from application.enums import Specialisation
class Activity(db.Model):
    __tablename__ = "activities"

    activity_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    location = db.Column(db.String(150), nullable=False)
    specialisation = db.Column(db.Enum(Specialisation), nullable=False)
    place_id = db.Column(db.Integer,db.ForeignKey('places.place_id') ,nullable=False)
    # guide_id = db.Column(db.Integer, db.ForeignKey('guide.guide_id'), nullable=False)
    description = db.Column(db.String(300), nullable=False)
    post_code = db.Column(db.String(300), nullable=False)

    def __init__(self, name, location, specialisation, place_id, description, post_code):
        self.name = name
        self.location = location
        self.specialisation = specialisation
        self.place_id = place_id
        # self.guide_id = guide_id
        self.description = description
        self.post_code = post_code

    @property
    def json(self):
        return {
            "activity_id": self.activity_id,
            "name": self.name,
            "location": self.location,
            "specialisation": self.specialisation,
            "place_id": self.place_id,
            # "guide_id": self.guide_id,
            "description": self.description,
            "post_code": self.post_code
        }
