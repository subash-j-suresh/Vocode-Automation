import os
from automation_clients.base_client import BaseClient


class AttioClient(BaseClient):
    def __init__(self) -> None:
        self.api_key = self.get_api_key()
        pass

    @classmethod
    def get_api_key(cls) -> str:
        return os.getenv("ATTIO_API_KEY")

    @classmethod
    def get_auth_token(cls):
        pass
