import logging
import os

LOG_DIR = "logs"
LOG_FILE = f"{LOG_DIR}/pipeline.log"

os.makedirs(LOG_DIR, exist_ok = True)

logging.basicConfig(
    filename = LOG_FILE,
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)



