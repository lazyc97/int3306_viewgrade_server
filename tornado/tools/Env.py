import os

import tornado.options


# debug mode
DEBUG = (os.environ["DEBUG"] == "1")

# key for JWT authentication
JWT_KEY = os.urandom(32)
if DEBUG:
    JWT_KEY = b"12345678"

# logging
tornado.options.options['log_file_prefix'] = '/var/log/tornado/app.log'
tornado.options.parse_command_line()
