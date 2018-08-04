import json
from .BaseApiHandler import BaseApiHandler

# for test purpose
class HelloController(BaseApiHandler):
    async def get(self):
        res = json.dumps({
            "response": "Hello, world",
        })
        self.write(res)
