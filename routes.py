from flask import Blueprint, request, jsonify
from .models import db, Episode, Guest, Appearance

api = Blueprint('api', __name__)
#homeroute
@api.route('/')
def home():
    return "Hello, welcome to lateshow"

#GET/episodes
@api.route('/episodes' , methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([e.to_dict() for e in episodes])

# GET /episodes/:id
@api.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get(id)
    if episode:
        return jsonify({
            **episode.to_dict(),
            "appearances": [a.to_dict() for a in episode.appearances]
        })
    return jsonify({"error": "Episode not found"}), 404

# GET /guests
@api.route('/guests', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    return jsonify([g.to_dict() for g in guests])

# POST /appearances
@api.route('/appearances', methods=['POST'])
def post_appearance():
    data = request.get_json()
    try:
        rating = int(data['rating'])
        Appearance.validate_rating(rating)

        new_app = Appearance(
            rating=rating,
            episode_id=data['episode_id'],
            guest_id=data['guest_id']
        )

        db.session.add(new_app)
        db.session.commit()

        return jsonify(new_app.to_dict()), 201

    except Exception as e:
        return jsonify({"errors": [str(e)]}), 400

# DELETE
@api.route('/episodes/<int:id>', methods=['DELETE'])
def delete_episode(id):
    episode = Episode.query.get(id)
    if episode:
        db.session.delete(episode)
        db.session.commit()
        return '', 204
    return jsonify({"error": "Episode not found"}), 404
