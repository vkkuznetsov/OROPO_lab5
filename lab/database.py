from neomodel import db
from lab.config import settings


def connect_to_database():
    """
    Устанавливает подключение к базе данных Neo4j с использованием настроек.
    """
    uri = f"bolt://{settings.DATABASE.USER}:{settings.DATABASE.PASSWORD}@{settings.DATABASE.URI}"

    try:
        db.set_connection(uri)
        print("Successfully connected to the Neo4j database.")
        return db
    except Exception as e:
        print(f"Failed to connect to the Neo4j database: {e}")

