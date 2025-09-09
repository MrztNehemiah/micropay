from flask import Flask, render_template, jsonify
from extensions import db, jwt
from auth import auth_bp
from users import users_bp


def create_app():
    app = Flask(__name__)
    app.config.from_prefixed_env()

    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)

    # Register blueprints
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(users_bp, url_prefix='/users')

    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return (
            jsonify(
                {
                    "message": "The token has expired",
                    "error": "token_expired"
                }
            )),401
    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return (
            jsonify(
                {
                    "message": "Signature verification failed",
                    "error": "invalid_token"
                }
            )),401
    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return (
            jsonify(
                {
                    "message": "Request does not contain an access token",
                    "error": "authorization_required"
                }
            )),401
    
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
if __name__ == "__main__":
    app = create_app()
    app.run()