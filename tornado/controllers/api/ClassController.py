import json

from bson.objectid import ObjectId

from .BaseApiHandler import BaseApiHandler


class ClassController(BaseApiHandler):
    # get classes by semester
    async def get(self):
        self.checkUserAccess()
        result = self.settings["db"]["classes"].find({
            "semesterId": ObjectId(self.json["semesterId"])
        })

        items = []
        async for item in result:
            item["_id"] = str(item["_id"])
            item["semesterId"] = str(item["semesterId"])
            items.append(item)

        self.write(json.dumps({
            "semesterId": self.json["semesterId"],
            "classes": items,
        }))


    # add a class
    async def post(self):
        self.checkAdminAccess()
        year = {
            "name": str(self.json["name"]),
            "code": str(self.json["code"]),
            "scorePdfLink": None,
            "semesterId": ObjectId(self.json["semesterId"]),
        }
        result = await self.settings["db"]["classes"].insert_one(year)
        self.write(json.dumps({
            "_id": str(result.inserted_id),
        }))


    # update a class
    async def put(self):
        self.checkAdminAccess()
        result = await self.settings["db"]["classes"].update_one({
            "_id": ObjectId(self.json["_id"]),
        }, {
            "$set": {
                "name": str(self.json["name"]),
                "code": str(self.json["code"]),
                "semesterId": ObjectId(self.json["semesterId"]),
            }
        })

        self.write(json.dumps({
            "modified": result.modified_count,
        }))


    # delete a class
    async def delete(self):
        self.checkAdminAccess()
        result = await self.settings["db"]["classes"].delete_one({
            "_id": ObjectId(self.json["_id"]),
        })

        self.write(json.dumps({
            "deleted": result.deleted_count,
        }))
