from error_handler.automation_exception import AutomationException
from error_handler.ErrorTypes import ErrorTypes


class PylonAutomatiionException(AutomationException):
    def __init__(self, error_code: int, error_message: str) -> None:
        super().__init__(error_code, ErrorTypes.PYLON_ERROR, error_message)
    