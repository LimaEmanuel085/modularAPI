from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import ASCENDING
import os

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://<db_username>:<db_password>@clusterapi.w58r7th.mongodb.net/?retryWrites=true&w=majority&appName=clusterApi")
client = AsyncIOMotorClient(MONGO_URL)
db =  clusterApi.task_db  # Nome do banco

# Acesso à coleção de tarefas
task_collection = db.tasks

