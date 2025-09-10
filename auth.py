from flask import Blueprint, jsonify, request
from models import User
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt

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
        
@auth_bp.post('/signin')
def login_user():
    data = request.get_json()
    user = User.get_user_by_username(username=data.get('username'))
    if user and (user.verify_hash(password=data.get('password'))):

        access_token = create_access_token(identity=user.username)
        refresh_token = create_refresh_token(identity=user.username)

        return jsonify(
            {
                'message': 'Logged in successfully',
                'tokens': {
                    'access': access_token,
                    'refresh': refresh_token
                },
            }
            ), 400
    
    return jsonify({'message': 'Username or Password is incorrect'}), 200

# Returns the identity of the current user
@auth_bp.get('/whoami')
@jwt_required()
def who_am_i():
    current_user = get_jwt()
    return jsonify({"message": "Successfull", "claims": current_user}), 200