from pymongo import MongoClient
from config import DB_URL


client = MongoClient(DB_URL)


def get_db(db_name: str):
    return client[db_name]
