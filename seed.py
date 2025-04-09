import csv
from models import db, Guest, Episode, Appearance
from datetime import datetime
from app import app

with app.app_context():
    db.drop_all()
    db.create_all()

    with open("/home/rency/Development/code/phase-4/lateshow-florence-simba/SEED DATA.csv", newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        episodes = {}
        guests = {}

        for row in reader:
            episode_date = row["Show"]

            ep_key = (episode_date)
            if ep_key not in episodes:
                episode = Episode(date=episode_date, number=int(row["YEAR"]))
                db.session.add(episode)
                db.session.flush()
                episodes[ep_key] = episode
            else:
                episode = episodes[ep_key]

            guest_name = row["Raw_Guest_List"]
            guest_occupation = row["GoogleKnowlege_Occupation"]
            guest_key = (guest_name, guest_occupation)
            if guest_key not in guests:
                guest = Guest(name=guest_name, occupation=guest_occupation)
                db.session.add(guest)
                db.session.flush()
                guests[guest_key] = guest
            else:
                guest = guests[guest_key]

            appearance = Appearance(
                rating=5,
                episode_id=episode.id,
                guest_id=guest.id
            )
            db.session.add(appearance)

        db.session.commit()

    print("Seeding successful.")