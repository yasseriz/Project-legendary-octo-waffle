import motor.motor_asyncio
from decouple import config
from bson.objectid import ObjectId

MONGO_DETAILS = config('mongoURI')
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
db = client.Series
basic_collection = db.get_collection("basicDetails")
# print(db)
print(basic_collection)