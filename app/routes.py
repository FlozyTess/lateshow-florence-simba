from flask import Blueprint, request, jsonify
from

api = Blueprint('api', __name__)

@api.route('/')
def index():
    return jsonify({ "message": "Welcome to the Late Show API" })
