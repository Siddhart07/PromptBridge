import mysql.connector
from dotenv import load_dotenv
import os

# Load env vars from .env file
load_dotenv(dotenv_path=".env")

def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        return conn
    except mysql.connector.Error as err:
        from utils.logger import get_logger
        logger = get_logger("db_connect")
        logger.error(f"Database connection failed: {err}")
        raise