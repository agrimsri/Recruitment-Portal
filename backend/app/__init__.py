import os
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from .config import config_map

load_dotenv()
from .extensions import db, api
from .models import *
from .resources import init_resources

def create_app(config_name=None):
    app = Flask(__name__, instance_relative_config=False)
    env = config_name or os.getenv('FLASK_ENV', 'development')
    app.config.from_object(config_map[env])

    # init extensions
    db.init_app(app)
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    
    # Initialize API and register resources
    init_resources(api)
    api.init_app(app)

    # Create database tables
    with app.app_context():
        db.create_all()

    return app
