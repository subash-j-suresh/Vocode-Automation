import logging
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
