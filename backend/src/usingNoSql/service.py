from motor.motor_asyncio import AsyncIOMotorClient
from config import settings


class NoSQLDatabase:
    def __init__(self):
        self.client = AsyncIOMotorClient(settings.MONGODB_URL)
        self.db = self.client[settings.MONGODB_DATABASE_NAME]

    async def add_logs(self, data):
        result = await self.db.logs.insert_one(data)
        info = await self.db.logs.find_one({"_id": result.inserted_id})
        if info:
            info["_id"] = str(info["_id"])
        return info
 


db = NoSQLDatabase()
