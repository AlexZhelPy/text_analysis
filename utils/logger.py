import logging
import os

def setup_logger():
    """
    Настройка логгера.
    :return: Объект логгера.
    """
    if not os.path.exists("logs"):
        os.makedirs("logs")

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler("logs/app.log"),
            logging.StreamHandler(),
        ],
    )
    return logging.getLogger(__name__)