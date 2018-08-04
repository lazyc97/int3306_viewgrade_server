import os

# debug mode
DEBUG = (os.environ["DEBUG"] == "1")

# key for JWT authentication
JWT_KEY = os.urandom(32)
if DEBUG:
    JWT_KEY = b"12345678"
