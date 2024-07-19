from functools import wraps
import logging
from error_handler.error_type import ErrorTypes
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
