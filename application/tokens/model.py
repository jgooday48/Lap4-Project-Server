from application import db
from datetime import datetime



class Token(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    jti = db.Column(db.String(), nullable=False)
    create_at = db.Column(db.DateTime(), default=datetime.utcnow)


    # def __repr__(self):
    #     return f"<Token {self.jti}>"
    
    def save(self): 
        db.session.add(self)
        db.session.commit()
