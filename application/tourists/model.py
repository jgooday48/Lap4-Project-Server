from application import db
from application.enums import UserType
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.dialects.postgresql import ARRAY

tourist_guide_association = db.Table(
    'tourist_guide',
    db.Column('tourist_id', db.Integer, db.ForeignKey('tourists.tourist_id')),
    db.Column('guide_id', db.Integer, db.ForeignKey('guides.guide_id'))
)


class Tourist(db.Model):
    __tablename__ = "tourists"

    tourist_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    user_type = db.Column(db.Enum(UserType), nullable=False)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(), nullable=False)
    password = db.Column(db.Text())
    images=db.Column(ARRAY(db.String()), nullable=True)
    plans = db.relationship('Plan', backref='tourist', lazy=True, foreign_keys='Plan.tourist_id')
    reviews = db.relationship('Review', backref='tourist', lazy=True, foreign_keys='Review.tourist_id')
    guides = db.relationship('Guide', secondary=tourist_guide_association, backref='tourists', lazy='dynamic')


    # def __repr__(self):
    #     return f"<User {self.username}"
    

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    @classmethod
    def get_user_by_email(cls, email): 
        return cls.query.filter_by(email = email).first()
    

    @classmethod
    def get_user_by_username(cls, username): 
        return cls.query.filter_by(username = username).first()
    
    def get_guides(self):
        return [g.json for g in self.guides]
    
    def add_guide(self, guide):
        if guide not in self.guides:
            self.guides.append(guide)
            db.session.commit()
    
    def remove_guide(self, guide):
        if guide in self.guides:
            self.guides.remove(guide)
            db.session.commit()
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.add(self)
        db.session.commit()
    
    @property
    def json(self):
        return {
            "tourist_id": self.tourist_id,
            "name": self.name,
            "user_type": self.user_type.name,  
            "username": self.username,
            "email": self.email,
            "password": self.password,
            "images": self.images
            # "guide_username": self.guide_username
        }




