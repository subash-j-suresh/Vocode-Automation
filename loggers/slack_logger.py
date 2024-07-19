import logging
import os
import requests


class SlackLoggerHandler(logging.Handler):
    def __init__(self, webhook_url):
        super().__init__()
        self.webhook_url = webhook_url

    def emit(self, record):
        log_entry = self.format(record)
        payload = {"message": log_entry}
        try:
            requests.post(self.webhook_url, json=payload)
        except Exception as e:
            print(f"Failed to send log to Slack: {e}")


def get_slack_logger(level=logging.INFO, webhook_url=None):
    if not webhook_url:
        webhook_url = os.getenv("SLACK_LOGGER_WEBHOOK")
    logger = logging.getLogger("slack_logger")
    logger.setLevel(level)

    slack_handler = SlackLoggerHandler(webhook_url)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    slack_handler.setFormatter(formatter)

    logger.addHandler(slack_handler)
    return logger
