from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    kafka_host: str = Field('localhost', env='KAFKA_HOST')
    kafka_port: str = Field('29092', env='KAFKA_PORT')
    project_name: str = Field('api kafka', env='PROJECT_NAME')

    jwt_secret: str = Field('test', env='JWT_SECRET')

    class Config:
        env_file = ".env"
