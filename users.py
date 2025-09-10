from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt
from models import User
from schemas import UserSchema


users_bp = Blueprint('users', __name__)

@users_bp.get('/allusers')
@jwt_required()
def get_users():
    claims = get_jwt()

    if claims.get('role') == 'admin':
        page = request.args.get('page', default=1, type=int)
        per_page = request.args.get('per_page', default=5, type=int)
        users = User.query.paginate(
            page = page,
            per_page = per_page
        )

        results = UserSchema().dump(users, many=True)
        return jsonify(
            {
                "Users": results
            }
        ), 200
    return jsonify({"message": "Admins only!"}), 401