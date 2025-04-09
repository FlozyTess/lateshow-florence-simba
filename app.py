from flask import Flask, request
from flask_migrate import Migrate
from flask_restful import Api, Resource
from models import db, Episode, Guest, Appearance

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///lateshow.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate = Migrate(app, db)
api = Api(app)

class IndexResource(Resource):
    def get(self):
        return {"message":"Welcome To Late Show API"}, 200

class EpisodeListResource(Resource):
    def get(self):
        episodes = Episode.query.all()
        return [ep.to_dict() for ep in episodes], 200

class EpisodeResource(Resource):
    def get(self, id):
        episode = Episode.query.get(id)
        if episode:
            return {
                "id": episode.id,
                "date": episode.date,
                "number": episode.number,
                "appearances": [a.to_dict() for a in episode.appearances]
            }, 200
        return {"error": "Episode not found"}, 404

class GuestListResource(Resource):
    def get(self):
        guests = Guest.query.all()
        return [g.to_dict() for g in guests], 200

class AppearanceResource(Resource):
    def post(self):
        data = request.get_json()
        try:
            rating = int(data.get("rating"))
            if rating < 1 or rating > 5:
                raise ValueError("Rating must be between 1 and 5")

            appearance = Appearance(
                rating=rating,
                episode_id=data["episode_id"],
                guest_id=data["guest_id"]
            )
            db.session.add(appearance)
            db.session.commit()
            return appearance.to_dict(), 201

        except Exception as e:
            return {"errors": [str(e)]}, 400

api.add_resource(IndexResource, "/")
api.add_resource(EpisodeListResource, "/episodes")
api.add_resource(EpisodeResource, "/episodes/<int:id>")
api.add_resource(GuestListResource, "/guests")
api.add_resource(AppearanceResource, "/appearances")

if __name__ == "__main__":
    app.run(debug=True)