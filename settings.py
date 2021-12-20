from decouple import config
from pydantic import BaseSettings

DB_MODELS = ["apps.user.models", 'apps.products.models', 'aerich.models']
SQLITE_DB_URL = f"postgres://postgres:{config('POSTGRES_PASSWORD')}@localhost:5432/app"


class TortoiseSettings(BaseSettings):
    """Tortoise-ORM settings"""

    db_url: str
    modules: dict
    generate_schemas: bool

    @classmethod
    def generate(cls):
        db_url = SQLITE_DB_URL
        modules = {"models": DB_MODELS}
        return TortoiseSettings(db_url=db_url,modules=modules,generate_schemas=True)
    
    @classmethod
    def migration_dict(cls):
        return {
    "connections": {"default": SQLITE_DB_URL},
    "apps": {
        "models": {
            "models": DB_MODELS,
            "default_connection": "default",
        },
    },
}