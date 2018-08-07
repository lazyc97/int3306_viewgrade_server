import json
import jwt
import tornado
from tools import Env

class BaseApiHandler(tornado.web.RequestHandler):
    def prepare(self):
        try:
            if len(self.request.body) > 0:
                self.json = json.loads(self.request.body)
            else:
                self.json = {}

            self.set_header("Content-Type", "application/json")
        except e:
            self.write("Cannot parse request content.")
            self.set_status(400)
            self.finish()

    def getUserId(self):
        userId = None
        strToken = self.request.headers.get("Authorization")

        if strToken is not None:
            try:
                token = bytes(strToken, encoding="utf-8")
                userId = jwt.decode(token, Env.JWT_KEY)["userId"]
            except:
                self.set_status(400)
                self.write("Invalid JWT token.")
                self.finish()

        return userId

    def checkUserAccess(self):
        if self.getUserId() is None:
            self.throwError(403)

    def checkAdminAccess(self):
        if self.getUserId() != self.settings["adminId"]:
            self.throwError(403)

    def throwError(self, errorCode):
        self.set_status(errorCode)
        self.finish()
