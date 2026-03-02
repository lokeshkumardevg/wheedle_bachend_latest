from flask import Blueprint, request, jsonify
from ..middleware.auth import token_required

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/dashboard', methods=['GET'])
@token_required
def dashboard(current_user):
    return jsonify({
        'message': 'Welcome Admin Dashboard',
        'adminId': str(current_user['_id'])
    })
