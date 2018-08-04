from motor.motor_tornado import MotorClient
from tornado.ioloop import IOLoop
from tornado.web import Application

from tools import Env
from controllers.api.HelloController import HelloController
from controllers.api.UserController import UserController
from controllers.api.ClassController import ClassController
from controllers.api.SemesterController import SemesterController
from controllers.api.YearController import YearController
from controllers.api.AuthController import AuthController


ROUTES = [
    (r"/api/hello", HelloController),
    (r"/api/user", UserController),
    (r"/api/class", ClassController),
    (r"/api/semester", SemesterController),
    (r"/api/year", YearController),
    (r"/api/auth", AuthController),
]

MONGO_CLIENT = MotorClient("database", 27017)
MONGO_DB = MONGO_CLIENT["viewgrade"]

if __name__ == "__main__":
    app = Application(ROUTES, debug=Env.DEBUG, db=MONGO_DB)
    app.listen(8000)
    IOLoop.current().start()
