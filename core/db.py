from pymongo import MongoClient
from config import db_url


client = MongoClient(db_url)


def get_db(db_name: str):
    return client[db_name]
