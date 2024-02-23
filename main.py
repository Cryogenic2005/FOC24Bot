import os
import logging
import logging.handlers

from telegram.ext import ApplicationBuilder
from dotenv import load_dotenv

import configs
from bot import handlers

if __name__ == "__main__":
    # Setup logging configurations
    log_levels_dict = {
        "critical": logging.CRITICAL,
        "error": logging.ERROR,
        "warning": logging.WARNING,
        "info": logging.INFO,
        "debug": logging.DEBUG,
    }
    log_level = getattr(configs, "LOG_LEVELS", "INFO") # Defaults to INFO if not set
    
    log_path = os.path.join("logs","bot.log")
    log_handler = logging.handlers.RotatingFileHandler(
        filename=log_path,
        maxBytes=10*2**20,
        backupCount=10
    )
    
    logging.basicConfig(
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%d-%b-%Y %H:%M:%S",
        level=log_level,
        handlers=[log_handler, logging.StreamHandler()],
    )
    
    # Get logger
    
    logger = logging.getLogger(__name__)
    
    # Setup bot configurations
    logger.info("Loading environment variables")
    load_dotenv()
    
    logger.info("Building bot")
    
    app = ApplicationBuilder().token(os.getenv("BOT_API_TOKEN")).build()
    for handler in handlers:
        app.add_handler(handler)
    
    logger.info("Starting bot")
    
    app.run_polling()    