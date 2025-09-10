from extensions import db
from uuid import uuid4
# Import necessary SQLAlchemy types
from sqlalchemy.dialects.postgresql import UUID
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

class User(db.Model):
    # Define the table name and columns
    __tablename__ = 'users'
    __table_args__ = {'schema': 'users'}
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(UUID(as_uuid=True), default=uuid4, unique=True)  # external identifier
    firstname = db.Column(db.String(150), nullable=False)
    lastname = db.Column(db.String(150), nullable=False)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'
    
    def generate_hash(self, password):
        self.password = generate_password_hash(password)

    def verify_hash(self, password):
        return check_password_hash(self.password, password)
    
    @classmethod
    def get_user_by_username(cls, username):
        return cls.query.filter_by(username=username).first()
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class TokenBlocklist(db.Model):
    __tablename__ = 'token_blocklist'
    __table_args__ = {'schema': 'users'}
    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(36), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self):
        return f'<TokenBlocklist {self.jti}>'
    
    def save(self):
        db.session.add(self)
        db.session.commit()