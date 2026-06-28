from pathlib import Path

PROJECT_ROOT = (
    Path(__file__)
    .resolve()
    .parent
    .parent
)

RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw"
PROCESSED_PATH = PROJECT_ROOT / "data" / "processed"
REJECTED_PATH = PROJECT_ROOT / "data" / "rejected"
CONFIG_PATH = PROJECT_ROOT / "config" / "config.yaml"
SQL_PATH = PROJECT_ROOT / "sql"





