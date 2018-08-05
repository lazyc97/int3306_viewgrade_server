from .BaseApiHandler import BaseApiHandler

class SemesterController(BaseApiHandler):
    # add a semester
    async def post(self):
        self.checkAdminAccess()
        pass

    # update a semester
    async def put(self):
        self.checkAdminAccess()
        pass

    # delete a semester
    async def delete(self):
        self.checkAdminAccess()
        pass
