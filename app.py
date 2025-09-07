from flask import Flask, render_template
from extensions import db


def create_app():
    app = Flask(__name__)
    app.config.from_prefixed_env()

    # Initialize extensions
    db.init_app(app)

    @app.route('/')
    @app.route('/home')
    def home():
        return render_template('home.html')

    @app.route('/signup')
    def signup():
        return render_template('signup.html')

    @app.route('/login')
    def login():
        return render_template('login.html')
    return app