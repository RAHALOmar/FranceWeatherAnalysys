import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler()
    ],  # maybe add a FileHandler in the future : logging.FileHandler("log_datetime.log")
)

logger = logging.getLogger(__name__)
