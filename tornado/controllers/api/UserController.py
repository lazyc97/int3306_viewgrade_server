import json

import jwt
from bson.objectid import ObjectId

from tools import Env
from tools.Encryption import getPasswordHash
from .BaseApiHandler import BaseApiHandler

class UserController(BaseApiHandler):
    # get user info
    async def get(self):
        userId = self.getUserId()
        if userId != self.json["_id"] and userId != self.settings["adminId"]:
            self.throwError(403)

        result = await self.settings["db"]["users"].find_one({
            "_id": ObjectId(self.json["_id"]),
        }, {
            "passwordHash": 0,
        })
        result["_id"] = str(result["_id"])

        self.write(json.dumps(result))


    # admin add user
    async def post(self):
        self.checkAdminAccess()
        user = {
            "username": str(self.json["username"]),
            "passwordHash": getPasswordHash(str(self.json["password"])),
            "subscribedClasses": [],
        }
        result = await self.settings["db"]["users"].insert_one(user)
        self.write(json.dumps({
            "_id": str(result.inserted_id),
        }))


    # user or admin change password
    async def put(self):
        userId = self.getUserId()
        if userId != self.json["_id"] and userId != self.settings["adminId"]:
            self.throwError(403)

        result = await self.settings["db"]["users"].update_one({
            "_id": ObjectId(userId),
        }, {
            "$set": {
                "passwordHash": getPasswordHash(str(self.json["password"])),
            }
        })

        self.write(json.dumps({
            "modified": result.modified_count,
        }))
