from functools import wraps
import logging
from exception_manager.error_types import ErrorTypes
from loggers.slack_logger import get_slack_logger


class AutomationException(Exception):
    def __init__(
        self,
        error_code: int,
        error_message: str,
        error_type: ErrorTypes = ErrorTypes.UNDEFINED_ERROR,
    ) -> None:
        self.message = error_message
        self.type = error_type
        self.code = error_code

    def __str__(self) -> str:
        return f"Error Code: {self.code}\nError Message: {self.message}"

    @classmethod
    def check_http_response(cls, status_code, response_data):
        if status_code not in [200, 201, 202]:
            raise cls(status_code, response_data)