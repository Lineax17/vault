"""database setup and utils"""

import sqlite3
from src.config import settings

DATABASE_SCHEMA = """--sql
    CREATE TABLE users (
        id STRING primary key,
        username STRING
    );

    CREATE TABLE password_entries (
        id INTEGER PRIMARY KEY,
        entry_name STRING,
        user_id STRING REFERENCES users(id),
        encrypted_password STRING
    );

    CREATE TABLE password_urls (
        id INTEGER PRIMARY KEY,
        url STRING
    );
"""

def get_database_schema_without_reset():
    """Only returns the table schema"""
    return DATABASE_SCHEMA

def get_database_schema_with_full_reset():
    """
    Retruns a table schema with drop table instructions
    to fully reset the db
    """
    return f"""
    DROP TABLE IF EXISTS users;
    DROP TABLE IF EXISTS password_entries;
    DROP TABLE IF EXISTS password_urls

    {DATABASE_SCHEMA}
    """


def get_connection():
    """Get a sqlite connection object to our database"""
    con = sqlite3.connect(str(settings.db_path))
    return con


def reset_db(con: sqlite3.Connection):
    """Executes a full reset to base schema of the database"""
    con.executescript(
        get_database_schema_with_full_reset()
    )
    con.commit()


def init_db():
    """Initializes the initial db"""
    con = get_connection()

    if not settings.db_path.exists():
        con.executescript(
            get_database_schema_without_reset()
        )
    else:
        print(f"Database file {settings.db_path} already exists -- delete to reset")
    con.close()
