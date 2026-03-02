from flask import Blueprint, request, jsonify
import os
import time
from werkzeug.utils import secure_filename
from bson.objectid import ObjectId

partner_bp = Blueprint('partner', __name__)

UPLOAD_FOLDER = 'uploads/'

@partner_bp.route('/', methods=['POST'])
def create_partner():
    try:
        from ..db import mongo
        data = {}
        if 'image' in request.files:
            file = request.files['image']
            if file.filename != '':
                filename = secure_filename(f"{int(time.time())}-{file.filename}")
                file.save(os.path.join(UPLOAD_FOLDER, filename))
                data['image'] = filename
        
        mongo.db.partners.insert_one(data)
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

@partner_bp.route('/', methods=['GET'])
def get_partners():
    try:
        from ..db import mongo
        partners = list(mongo.db.partners.find())
        for p in partners:
            p['_id'] = str(p['_id'])
        return jsonify(partners)
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@partner_bp.route('/<id>', methods=['DELETE'])
def delete_partner(id):
    try:
        from ..db import mongo
        mongo.db.partners.delete_one({"_id": ObjectId(id)})
        return jsonify({'message': 'Deleted'})
    except Exception as e:
        return jsonify({'message': str(e)}), 500
