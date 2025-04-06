from flask import Blueprint, jsonify

api = Blueprint('api', __name__)

@api.route('/')
def index():
    return jsonify({ "message": "Welcome to the Late Show API" })
