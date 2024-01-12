from application import db

class Review(db.Model):
    review_id = db.Column(db.Integer, primary_key=True)
    guide_id = db.Column(db.Integer, db.ForeignKey('guides.guide_id'), nullable=False)
    tourist_id = db.Column(db.Integer, db.ForeignKey('tourists.tourist_id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String(500), nullable=True)


    def __init__(self, guide_id,tourist_id, rating, comment):
        self.guide_id = guide_id
        self.tourist_id = tourist_id
        self.rating = rating
        self.comment = comment

    @property
    def json(self):
        return {
            "review_id": self.review_id,
            "guide_id": self.guide_id,
            "tourist_id": self.tourist_id,
            "rating": self.rating,
            "comment": self.comment
        }
