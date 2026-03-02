from flask_bcrypt import Bcrypt
import jwt
import datetime
from ..config import JWT_SECRET

bcrypt = Bcrypt()

def hash_password(password):
    return bcrypt.generate_password_hash(password).decode('utf-8')

def check_password(hashed_password, password):
    return bcrypt.check_password_hash(hashed_password, password)

def generate_token(user_id):
    payload = {
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
        'iat': datetime.datetime.utcnow(),
        'id': str(user_id)
    }
    return jwt.encode(payload, JWT_SECRET, algorithm='HS256')
