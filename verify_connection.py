import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')
print(DATABASE_URL)
assert DATABASE_URL, "DATABASE_URL is not set"

client = MongoClient(DATABASE_URL)
db = client.get_database()

print("Collections:", db.list_collection_names())
