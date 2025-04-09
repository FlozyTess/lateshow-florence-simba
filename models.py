from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# episode Model
class Episode(db.Model): 
    __tablename__ = 'episodes'
    
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String, nullable=False) 
    number = db.Column(db.Integer, nullable=False)

    # relationship with Appearance
    appearances = db.relationship('Appearance', backref='episode', cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "id":self.id,
            "date":self.date,
            "number":self.number,
        } 
    
    #guest Model
class Guest(db.Model):
    __tablename__ = 'guests'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    occupation = db.Column(db.String, nullable=False)

    #  relationship with Appearance
    appearances = db.relationship('Appearance', backref='guest', cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "occupation": self.occupation,
        }

# appearance Model 
class Appearance(db.Model):
    __tablename__ = 'appearances'

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'), nullable=False)
    guest_id = db.Column(db.Integer, db.ForeignKey('guests.id'), nullable=False)

    @staticmethod
    def validate_rating(value):
        if not 1 <= value <= 5:
            raise ValueError("Rating must be between 1 and 5.")

    def to_dict(self):
        return {
            "id": self.id,
            "rating": self.rating,
            "guest_id": self.guest_id,
            "episode_id": self.episode_id,
            "guest": self.guest.to_dict(),
            "episode": self.episode.to_dict()
        }

print("models successful.")
