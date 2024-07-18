import requests
from error_handler.error_type import ErrorTypes


class AutomationException(Exception):
    def __init__(self, error_code :int, error_type :ErrorTypes, error_message :str) -> None:
        self.message = error_message
        self.type = error_type
        self.code = error_code
    
    def __str__(self) -> str:
        return f"{self.type.value} Error Code: {self.code}\nError Message: {self.message}"

    @classmethod
    def log_error(cls, e: Exception):
        SLACK_WEBHOOK = "https://hooks.slack.com/triggers/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"

        payload = {
        "message": f"{e}"
        }
        response = requests.request("POST", SLACK_WEBHOOK, json=payload)
        return response