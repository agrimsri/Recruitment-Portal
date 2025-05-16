import os
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from .config import config_map

load_dotenv()
from .extensions import db, api
from .resources.todo import TodoList, TodoItem

def create_app(config_name=None):
    app = Flask(__name__, instance_relative_config=False)
    env = config_name or os.getenv('FLASK_ENV', 'development')
    app.config.from_object(config_map[env])

    # init extensions
    db.init_app(app)
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    
    # Initialize API and add resources
    from .resources.webhooks import ClerkWebhook
    api.add_resource(TodoList, '/api/todos')
    api.add_resource(TodoItem, '/api/todos/<int:todo_id>')
    api.add_resource(ClerkWebhook, '/api/webhooks/clerk/user')
    api.init_app(app)

    # Create database tables
    with app.app_context():
        db.create_all()

    return app
