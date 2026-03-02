from ..db import mongo
from bson.objectid import ObjectId
from datetime import datetime

class Blog:
    @staticmethod
    def create(data):
        data['createdAt'] = datetime.utcnow()
        return mongo.db.blogs.insert_one(data)

    @staticmethod
    def find_all():
        return list(mongo.db.blogs.find())

    @staticmethod
    def find_by_slug(slug):
        return mongo.db.blogs.find_one({"slug": slug})

    @staticmethod
    def find_by_id(id):
        return mongo.db.blogs.find_one({"_id": ObjectId(id)})

class Job:
    @staticmethod
    def create(data):
        data['createdAt'] = datetime.utcnow()
        data['updatedAt'] = datetime.utcnow()
        return mongo.db.jobs.insert_one(data)

    @staticmethod
    def find_all():
        return list(mongo.db.jobs.find())

class Admin:
    @staticmethod
    def find_by_email(email):
        return mongo.db.admins.find_one({"email": email})

    @staticmethod
    def find_by_id(id):
        return mongo.db.admins.find_one({"_id": ObjectId(id)}) 

    @staticmethod
    def create(data):
        return mongo.db.admins.insert_one(data)

class Contact:
    @staticmethod
    def create(data):
        data['createdAt'] = datetime.utcnow()
        data['updatedAt'] = datetime.utcnow()
        data.setdefault('status', 'Pending')
        return mongo.db.contacts.insert_one(data)

    @staticmethod
    def find_all():
        return list(mongo.db.contacts.find())
