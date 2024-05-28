from motor.core import AgnosticClient
from motor.motor_asyncio import AsyncIOMotorClient
from store.core.config import settings

class MongoClient:
    def __init__(self) -> None:
        self.client: AgnosticClient = AsyncIOMotorClient(
            settings.DATABASE_URL,
            uuidRepresentation='standard'  # Corrected the value
        )

    def get(self) -> AgnosticClient:
        return self.client

db_client = MongoClient()
