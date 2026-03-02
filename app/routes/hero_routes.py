from flask import Blueprint, request, jsonify
from bson.objectid import ObjectId

hero_bp = Blueprint('hero', __name__)

@hero_bp.route('/', methods=['GET'])
def get_hero():
    try:
        from ..db import mongo
        hero = mongo.db.hero.find_one()
        if hero:
            hero['_id'] = str(hero['_id'])
        return jsonify(hero)
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@hero_bp.route('/', methods=['PUT'])
def update_hero():
    try:
        data = request.get_json()
        from ..db import mongo
        updated = mongo.db.hero.find_one_and_update(
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
