import asyncio

from motor.motor_tornado import MotorClient
from tornado.ioloop import IOLoop
from tornado.web import Application

from tools import Env, Init
from controllers.api.HelloController import HelloController
from controllers.api.UserController import UserController
from controllers.api.ClassController import ClassController
from controllers.api.SemesterController import SemesterController
from controllers.api.YearController import YearController
from controllers.api.AuthController import AuthController
from controllers.api.FileUploadController import FileUploadController


ROUTES = [
    (r"/api/hello/", HelloController),
    (r"/api/user/", UserController),
    (r"/api/class/", ClassController),
    (r"/api/semester/", SemesterController),
    (r"/api/year/", YearController),
    (r"/api/auth/", AuthController),
    (r"/api/fileupload/", FileUploadController),
]

MONGO_URI = "mongodb://{0}:{1}@database:27017/admin".format("root", "root")
MONGO_CLIENT = MotorClient(MONGO_URI)
MONGO_DB = MONGO_CLIENT["viewgrade"]

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    app = Application(ROUTES, xheaders=True, debug=Env.DEBUG, db=MONGO_DB)
    loop.run_until_complete(Init.init(app))
    app.listen(8000)
    IOLoop.current().start()
