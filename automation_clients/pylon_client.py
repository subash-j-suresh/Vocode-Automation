import requests
import os

from automation_clients.base_client import BaseClient
from error_handler.custom_exceptions.http_exception import HTTPException
from error_handler.custom_exceptions.pylon_exception import PylonException


class PylonClient(BaseClient):
    # Constants
    PYLON_ACCOUNTS_URL = "https://api.usepylon.com/accounts"

    def __init__(self) -> None:
        self.api_key = PylonClient.get_api_key()
        self.api_headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

    @classmethod
    def get_api_key(cls):
        return os.getenv("PYLON_API_KEY")

    def get_accounts(self) -> list[dict]:
        response = requests.get(self.PYLON_ACCOUNTS_URL, headers=self.api_headers)
        if response.status_code != 200:
            raise PylonException(
                -1,
                "Failed to retrive the pylon accounts request returned error code: {response.status_code}",
            )

        return response.json().get("data", [])

    def get_account(self, account_name: str) -> dict:
        accounts = self.get_accounts()
        account = next((acc for acc in accounts if acc["name"] == account_name), None)
        if account is None:
            raise PylonException(
                -1, "Account not found in python, please check your company name input"
            )
        return account

    def update_account(self, account_id, payload):
        account_url = f"{self.PYLON_ACCOUNTS_URL}/{account_id}"
        response = requests.patch(account_url, json=payload, headers=self.api_headers)
        HTTPException.check_error(response=response)
        return response
