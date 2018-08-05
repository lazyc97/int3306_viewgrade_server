import json

from bson.objectid import ObjectId

from .BaseApiHandler import BaseApiHandler


class YearController(BaseApiHandler):
    # get info of years
    async def get(self):
        self.checkUserAccess()
        result = self.settings["db"]["years"].find({})

        items = []
        async for item in result:
            item["_id"] = str(item["_id"])
            items.append(item)

        self.write(json.dumps({
            "years": items
        }))


    # add a university year
    async def post(self):
        self.checkAdminAccess()
        year = {
            "startYear": int(self.json["startYear"]),
        }
        result = await self.settings["db"]["years"].insert_one(year)
        self.write(json.dumps({
            "_id": str(result.inserted_id),
        }))


    # update a university year
    async def put(self):
        self.checkAdminAccess()
        result = await self.settings["db"]["years"].update_one({
            "_id": ObjectId(self.json["_id"]),
        }, {
            "$set": {
                "startYear": int(self.json["startYear"]),
            }
        })

        self.write(json.dumps({
            "modified": result.modified_count,
        }))


    # delete a university year
    async def delete(self):
        self.checkAdminAccess()
        result = await self.settings["db"]["years"].delete_one({
            "_id": ObjectId(self.json["_id"]),
        })

        self.write(json.dumps({
            "deleted": result.deleted_count,
        }))
