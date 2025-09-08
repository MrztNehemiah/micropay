from extensions import db
from uuid import uuid4
# Import necessary SQLAlchemy types
from sqlalchemy.dialects.postgresql import UUID

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