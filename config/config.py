import os
from dotenv import load_dotenv

load_dotenv()

class Config:

    AZURE_CONNECTION_STRING = os.getenv(
        "AZURE_STORAGE_CONNECTION_STRING"
    )

    CONTAINER_NAME = os.getenv(
        "AZURE_CONTAINER_NAME"
    )

    DATABRICKS_HOST = os.getenv(
        "DATABRICKS_HOST"
    )

    DATABRICKS_TOKEN = os.getenv(
        "DATABRICKS_TOKEN"
    )

    DATABASE_NAME = os.getenv(
        "DATABASE_NAME",
        "monitoring.db"
    )

    LOG_LEVEL = os.getenv(
        "LOG_LEVEL",
        "INFO"
    )
    JOB_NAME = os.getenv(
        "JOB_NAME",
        "Default Job"
    )
    TEAMS_WEBHOOK = os.getenv("TEAMS_WEBHOOK")


