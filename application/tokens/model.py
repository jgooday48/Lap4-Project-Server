from datetime import datetime


def get_token_model():
   from application import db


   class Token(db.Model):
      __tablename__ = "tokens"
      id = db.Column(db.Integer(), primary_key=True)
      jti = db.Column(db.String(), nullable=False)
      create_at = db.Column(db.DateTime(), default=datetime.utcnow)
      
      def __repr__(self):
        return f"<Token {self.jti}>"
      
      def save(self):
         db.session.add(self)
         db.session.commit()
      
   return Token
