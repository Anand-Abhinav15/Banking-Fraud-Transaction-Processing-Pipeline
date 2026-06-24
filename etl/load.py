from sqlalchemy import create_engine
from dotenv import load_dotenv

import os

from etl.logger import logger

load_dotenv()


def get_engine():

    user = os.getenv("POSTGRES_USER")
    password = os.getenv("POSTGRES_PASSWORD")
    host = os.getenv("POSTGRES_HOST")
    port = os.getenv("POSTGRES_PORT")
    db = os.getenv("POSTGRES_DB")

    connection_string = (
        f"postgresql://{user}:{password}"
        f"@{host}:{port}/{db}"
    )

    return create_engine(connection_string)








