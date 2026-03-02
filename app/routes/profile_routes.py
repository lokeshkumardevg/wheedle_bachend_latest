from flask import Blueprint, request, jsonify
from bson.objectid import ObjectId

profile_bp = Blueprint('profile', __name__)

@profile_bp.route('/', methods=['GET'])
def get_profile():
    try:
        from ..db import mongo
        profile = mongo.db.profiles.find_one()
        if profile:
            profile['_id'] = str(profile['_id'])
        return jsonify(profile)
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@profile_bp.route('/', methods=['PUT'])
def update_profile():
    try:
        data = request.get_json()
        from ..db import mongo
        updated = mongo.db.profiles.find_one_and_update(
            {},
            {"$set": data},
            upsert=True,
            return_document=True
        )
        if updated:
            updated['_id'] = str(updated['_id'])
        return jsonify(updated)
    except Exception as e:
        return jsonify({'message': str(e)}), 500
