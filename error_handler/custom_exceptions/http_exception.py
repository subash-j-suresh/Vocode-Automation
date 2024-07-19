from error_handler.custom_exceptions.automation_exception import AutomationException
from error_handler.error_type import ErrorTypes
from requests import Response


class HTTPException(AutomationException):
    def __init__(self, status_code: int, error_message: str) -> None:
        super().__init__(status_code, ErrorTypes.HTTP_ERROR, error_message)

    def __str__(self) -> str:
        return f"HTTP Error status code {self.code}\nError Message: {self.message}"

    @classmethod
    def check_error(cls, response: Response):
        if response.status_code not in [200, 201, 202]:
            raise HTTPException(response.status_code, response.json())
