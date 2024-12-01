from motor.motor_asyncio import AsyncIOMotorClient

# MongoDB URI (change to your MongoDB connection string)
MONGO_URI = "mongodb+srv://rohit:rohit123@cluster0.lcb7d.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Initialize MongoDB client
client = AsyncIOMotorClient(MONGO_URI)

# Access the database
db = client["testdb"]

# Access specific collections
product_collection = db["product_collection"]

# Close the MongoDB connection on shutdown (optional but recommended)
async def close_db_connection():
    client.close()
