import os
import json

from bson.objectid import ObjectId

from .BaseApiHandler import BaseApiHandler


class FileUploadController(BaseApiHandler):
    async def post(self):
        self.checkAdminAccess()

        classId = ObjectId(self.get_body_argument("classId"))
        fileInfo = self.request.files["scorePdf"][0]
        filePath = "/storage/pdf/{}.pdf".format(str(classId))
        with open(filePath, "wb") as output:
            output.write(fileInfo["body"])

        result = await self.settings["db"]["classes"].update_one({
            "_id": classId
        }, {
            "$set": {
                "scorePdfLink": filePath
            },
        })

        self.write(json.dumps({
            "modified": result.modified_count,
        }))

    async def delete(self):
        self.checkAdminAccess()

        classId = ObjectId(self.get_argument("classId"))
        filePath = "/storage/pdf/{}.pdf".format(str(classId))
        os.remove(filePath)
        result = await self.settings["db"]["classes"].update_one({
            "_id": classId
        }, {
            "$set": {
                "scorePdfLink": None
            },
        })

        self.write(json.dumps({
            "modified": result.modified_count,
        }))
