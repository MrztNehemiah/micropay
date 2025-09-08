from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

# Create SQLAlchemy instance
db = SQLAlchemy()

# Create JWT Manager instance
jwt = JWTManager()