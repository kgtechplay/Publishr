from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    env: str = 'development'
    database_url: str = 'sqlite:///publishr.db'

settings = Settings()
