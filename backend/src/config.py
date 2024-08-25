from functools import lru_cache
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    BASE_URL : str

    REDIS_HOST : str
    REDIS_PORT : int

    MONGODB_URL : str
    MONGODB_DATABASE_NAME : str

    POSTGRES_USER : str 
    POSTGRES_PASSWORD : str
    POSTGRES_DB : str
    POSTGRES_HOST : str
    POSTGRES_PORT : str

    POSTGRES_URL : str
    
    class Config:
        env_file = ".env"

@lru_cache()
def get_settings() -> Settings:
    return Settings()

settings = get_settings()