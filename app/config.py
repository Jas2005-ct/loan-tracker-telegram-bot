from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    telegram_bot_token: str
    openrouter_api_key: str | None = None
    openrouter_model: str = "openrouter/free"
    database_url: str = "sqlite:///./loan_tracker.db"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
