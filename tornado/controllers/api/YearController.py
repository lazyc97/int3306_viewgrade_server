from .BaseApiHandler import BaseApiHandler

class YearController(BaseApiHandler):
    # get years/semesters layout
    async def get(self):
        pass

    # add a university year
    async def post(self):
        await self.checkAdminAccess()
        pass

    # update a university year
    async def put(self):
        await self.checkAdminAccess()
        pass

    # delete a university year
    async def delete(self):
        await self.checkAdminAccess()
        pass
