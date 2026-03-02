from flask import Blueprint, request, jsonify
from ..models import Admin
from ..utils.auth import check_password, generate_token
import jwt
from ..config import JWT_SECRET

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return jsonify({'message': 'Email and password are required'}), 400

        admin = Admin.find_by_email(email)
        if not admin:
            return jsonify({'message': 'Admin not found'}), 400

        if not check_password(admin['password'], password):
            return jsonify({'message': 'Invalid password'}), 400

        token = generate_token(admin['_id'])

        return jsonify({
            'message': 'Login success',
            'token': token
        })

    except Exception as e:
        return jsonify({'message': str(e)}), 500

@auth_bp.route('/verify', methods=['GET'])
def verify():
    try:
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Bearer '):
            return jsonify({'message': 'No token'}), 401

        token = auth_header.split(" ")[1]
        decoded = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])

        return jsonify({
            'message': 'Valid',
            'id': decoded['id']
        })

    except Exception:
        return jsonify({'message': 'Invalid token'}), 401
