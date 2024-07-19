from exception_manager.custom_exceptions.automation_exception import AutomationException
from exception_manager.error_types import ErrorTypes


class PylonException(AutomationException):
    def __init__(self, error_code: int, error_message: str) -> None:
        super().__init__(
            error_code=error_code,
            error_type=ErrorTypes.PYLON_ERROR,
            error_message=error_message,
        )

    def __str__(self) -> str:
        return super().__str__()
