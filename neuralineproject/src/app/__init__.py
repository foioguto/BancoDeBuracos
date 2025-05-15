from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://usuario:senha@localhost:5432/nome_do_banco'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db = SQLAlchemy(app)

    class TODO(db.model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(100), nullable=False)
        completed = db.Column(db.Boolean, default=False)
        date_created = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return '<Task %r>' % self.id


    @app.route('/')
    def index():
        return render_template('index.html')

    return app
