from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    JIRA_URL: str
    GITLAB_URL: str
    GITLAB_TOKEN: str
    JIRA_TOKEN: str
    SLURM_URL: str

    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: str

    @property
    def db_url(self):
        return f"postgresql+psycopg2://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
