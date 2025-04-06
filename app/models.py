from datetime import datetime
from app import db

# episode Model
class Episode(db.Model):
    __tablename__ = 'episodes'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(20), nullable=False)
    number = db.Column(db.Integer, nullable=False)

    # relationship with Appearance
    appearances = db.relationship('Appearance', backref='episode', cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Episode {self.number} - {self.date}>"

# guest Model
class Guest(db.Model):
    __tablename__ = 'guests'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    occupation = db.Column(db.String(100), nullable=False)

    #  relationship with Appearance
    appearances = db.relationship('Appearance', backref='guest', cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Guest {self.name}>"

# appearance Model (Join table)
class Appearance(db.Model):
    __tablename__ = 'appearances'

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)

    # foreign Keys
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'), nullable=False)
    guest_id = db.Column(db.Integer, db.ForeignKey('guests.id'), nullable=False)

    def __repr__(self):
        return f"<Appearance {self.id} - Guest {self.guest.name} on Episode {self.episode.number}>"

