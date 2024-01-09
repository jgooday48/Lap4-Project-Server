from application import db

class Place(db.Model):
    __tablename__ = "places"

    place_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    location = db.Column(db.String(150), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    tags = db.Column(db.String(150), nullable=False)

    def __init__(self, name, location, description, tags):
        self.name = name
        self.location = location
        self.description = description
        self.tags = tags

    @property
    def json(self):
        return {
            "place_id": self.place_id,
            "name": self.name,
            "location": self.location,
            "description": self.description,
            "tags": self.tags
        }

