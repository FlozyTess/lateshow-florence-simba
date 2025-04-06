import csv
from app.models import db, Guest, Episode

def seed_data():
    with open('guests.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            guest = Guest(name=row['name'], occupation=row['occupation'])
            db.session.add(guest)

    episode1 = Episode(date="1/11/99", number=1)
    episode2 = Episode(date="1/12/99", number=2)
    db.session.add_all([episode1, episode2])
    db.session.commit()