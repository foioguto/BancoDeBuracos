from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://usuario:senha@localhost:5432/nome_do_banco'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db = db.init_app(app)

    from .drive_controller import main 
    app.register_blueprint(main)
    
    @app.route('/')
    def index():
        return render_template('index.html')

    return app
