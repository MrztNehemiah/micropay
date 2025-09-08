from flask import Blueprint, jsonify, request
from models import User

auth_bp = Blueprint('auth', __name__)

@auth_bp.post('/signup')
def status():

    data = request.get_json()

    user = User.get_user_by_username(username=data.get('username'))

    if user is not None:
        return jsonify({"message": "User already exists"}), 403
    
    new_user = User(
        firstname=data.get('firstname'),
        lastname=data.get('lastname'),
        username=data.get('username'),
        email=data.get('email')
    )
    new_user.generate_hash(data.get('password'))

    new_user.save()
    
    return jsonify({"message": "User created successfully"}), 201
        