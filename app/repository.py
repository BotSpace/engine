import motor.motor_asyncio

from app.config import MONGO_URL

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)
db = client["bot"]


async def get_or_create_user(chat_id):
    collection = db["users"]
    user = await collection.find_one({"chat_id": chat_id})
    if user:
        return user
    print("foydalanuvchi yaratildi")
    return await collection.insert_one(
        {
            "chat_id": chat_id,
        }
    )


async def exists_user(chat_id):
    collection = db["users"]
    user = await collection.find_one({"chat_id": chat_id})
    return user is not None
