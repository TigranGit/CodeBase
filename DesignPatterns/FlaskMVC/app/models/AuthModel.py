from ..app import mongo
import hashlib
from flask_pymongo import ObjectId
from datetime import datetime
from app.helpers.utils import to_dictionary_array


class AuthModel:
    def __init__(self):
        pass

    def getUser(_id):
        users = mongo.db.users.find({"_id": _id})
        x = []
        for user in users:
            x.append(user)
        return user

    def getAllUser(_id):
        users = mongo.db.users.find()
        return to_dictionary_array(users)

    def registerUser(self, _first_name, _last_name, _email, _password):
        d = datetime.now()
        h = hashlib.md5(_password.encode())
        insertdata = {
            "first_name": _first_name,
            "last_name": _last_name,
            "email": _email,
            "password": h.hexdigest(),
            "status": "0",
            "created_at": d,
            "updated_at": d,
        }
        u = mongo.db.users.insert(insertdata)
        return {
            "status": "1",
            "message": "Registration Successfull",
            "_id": str(ObjectId(u)),
        }


authmodel = AuthModel()
