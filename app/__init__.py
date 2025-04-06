from flask import Flask
from flask_migrate import Migrate
from .models import db

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lateshow.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app) 
    migrate(app, db)

    from .routes import api
    app.register_blueprint(api)

    return app

app = create_app()

