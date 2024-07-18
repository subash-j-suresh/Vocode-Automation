from enum import Enum

class ErrorTypes(Enum):
    HTTP_ERROR = "HTTP Error"
    PYLON_ERROR = "Error when handling pylon"
    ATTIO_ERROR = "Error when handling Attio"
    UNDEFINED_ERROR = "Unhandled Exception"