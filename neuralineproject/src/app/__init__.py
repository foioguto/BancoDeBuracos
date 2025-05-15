from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .utils.config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    
    from app.controllers.database_controller import db_controller
    from app.controllers.drive_controller import drive_controller
    from app.controllers.geocoding_controller import geo_controller
    from app.controllers.metadata_controller import meta_controller
    
    app.register_blueprint(db_controller)
    app.register_blueprint(drive_controller)
    app.register_blueprint(geo_controller)
    app.register_blueprint(meta_controller)
    
    return app