from application import db

class Review(db.Model):
    review_id = db.Column(db.Integer, primary_key=True)
    guide_id = db.Column(db.Integer, db.ForeignKey('guides.guide_id'), nullable=False)
    tourist_id = db.Column(db.Integer, db.ForeignKey('tourists.tourist_id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String())
    comment = db.Column(db.String(), nullable=True)
    timestamp = db.Column(db.DateTime())


    def __init__(self, guide_id,tourist_id, rating, title, comment, timestamp):
        self.guide_id = guide_id
        self.tourist_id = tourist_id
        self.rating = rating
        self.title = title
        self.comment = comment
        self.timestamp = timestamp

    @property
    def json(self):
        return {
            "review_id": self.review_id,
            "guide_id": self.guide_id,
            "tourist_id": self.tourist_id,
            "rating": self.rating,
            "title": self.title,
            "comment": self.comment,
            "timestamp": self.timestamp
        }
