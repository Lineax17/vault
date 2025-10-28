from pathlib import Path


class Settings:
    db_path = Path('database.db')

def get_settings():
    return Settings()

settings = get_settings()
