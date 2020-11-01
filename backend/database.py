import motor.motor_asyncio
from decouple import config

MONGO_DETAILS = config('mongoURI')
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
db = client.Series
basic_collection = db.get_collection("basicDetails")

# helper functions
def series_helper(series)->dict:
    return {
        "id": str(series["_id"]),
        "name": series["name"],
        "source": series["source"],
        "link": series["link"],
    }
