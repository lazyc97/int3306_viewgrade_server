from .BaseApiHandler import BaseApiHandler

class ClassController(BaseApiHandler):
    # get classes by semester
    async def get(self):
        pass

    # add a class
    async def post(self):
        await self.checkAdminAccess()
        pass

    # update a class
    async def put(self):
        await self.checkAdminAccess()
        pass

    # delete a class
    async def delete(self):
        await self.checkAdminAccess()
        pass
