import json
from datetime import datetime

from bson.objectid import ObjectId

from .BaseApiHandler import BaseApiHandler


class SemesterController(BaseApiHandler):
    # get semesters by year
    async def get(self):
        self.checkUserAccess()
        result = self.settings["db"]["semesters"].find({
            "yearId": ObjectId(self.json["yearId"])
        })

        items = []
        async for item in result:
            item["_id"] = str(item["_id"])
            item["startDate"] = datetime.strftime(item["startDate"], "%Y-%m-%d")
            item["yearId"] = str(item["yearId"])
            items.append(item)

        self.write(json.dumps({
            "yearId": self.json["yearId"],
            "semesters": items,
        }))


    # add a semester
    async def post(self):
        self.checkAdminAccess()
        year = {
            "name": str(self.json["name"]),
            "startDate": datetime.strptime(self.json["startDate"], "%Y-%m-%d"),
            "yearId": ObjectId(self.json["yearId"]),
        }
        result = await self.settings["db"]["semesters"].insert_one(year)
        self.write(json.dumps({
            "_id": str(result.inserted_id),
        }))


    # update a semester
    async def put(self):
        self.checkAdminAccess()
        result = await self.settings["db"]["semesters"].update_one({
            "_id": ObjectId(self.json["_id"]),
        }, {
            "$set": {
                "name": str(self.json["name"]),
                "startDate": datetime.strptime(self.json["startDate"], "%Y-%m-%d"),
                "yearId": ObjectId(self.json["yearId"]),
            }
        })

        self.write(json.dumps({
            "modified": result.modified_count,
        }))


    # delete a semester
    async def delete(self):
        self.checkAdminAccess()
        result = await self.settings["db"]["semesters"].delete_one({
            "_id": ObjectId(self.json["_id"]),
        })

        self.write(json.dumps({
            "deleted": result.deleted_count,
        }))
