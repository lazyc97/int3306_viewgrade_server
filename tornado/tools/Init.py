from .Encryption import getPasswordHash

async def createAdminUser(app):
    db = app.settings["db"]
    result = await db["users"].find_one({
        "username": "admin"
    })

    if result is None:
        result = await db["users"].insert_one({
            "username": "admin",
            "passwordHash": getPasswordHash("admin"),
            "subscribedClasses": [],
        })
        app.settings["adminId"] = result.inserted_id
    else:
        app.settings["adminId"] = result["_id"]


async def init(app):
    await createAdminUser(app)
