import logging
import os

from loggers.log_handlers.slack_log_handler import SlackLoggerHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# configure slack logger
webhook_url = os.getenv("SLACK_LOGGER_WEBHOOK")
slack_handler = SlackLoggerHandler(webhook_url)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
slack_handler.setFormatter(formatter)
logger.addHandler(slack_handler)
