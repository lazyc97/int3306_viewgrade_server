from .BaseApiHandler import BaseApiHandler

class SemesterController(BaseApiHandler):
    # add a semester
    async def post(self):
        await self.checkAdminAccess()
        pass

    # update a semester
    async def put(self):
        await self.checkAdminAccess()
        pass

    # delete a semester
    async def delete(self):
        await self.checkAdminAccess()
        pass
