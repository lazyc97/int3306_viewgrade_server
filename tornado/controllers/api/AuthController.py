import json

import jwt

from tools.Encryption import verifyPassword
from tools.Env import JWT_KEY
from .BaseApiHandler import BaseApiHandler


class AuthController(BaseApiHandler):
    # login
    async def post(self):
        result = await self.settings["db"]["users"].find_one({
            "username": str(self.json["username"])
        })
        if verifyPassword(self.json["password"], result["passwordHash"]):
            token = jwt.encode({
                "userId": str(result["_id"])
            }, JWT_KEY)
            self.write(json.dumps({ "token": token.decode("utf-8") }))
        else:
            self.throwError(400)

