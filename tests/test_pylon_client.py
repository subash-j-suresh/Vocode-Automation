import pytest
import os
from unittest.mock import patch, Mock
from automation_clients.pylon_client import PylonClient
from error_handler.custom_exceptions.pylon_exception import PylonException
from error_handler.custom_exceptions.http_exception import HTTPException

@pytest.fixture
def mock_env():
    os.environ['PYLON_API_KEY'] = 'test_api_key'
    yield
    del os.environ['PYLON_API_KEY']

@patch('requests.get')
def test_get_accounts_SuccessfulResponse_ReturnsAccounts(mock_get, mock_env):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"data": [{"name": "account1"}, {"name": "account2"}]}
    mock_get.return_value = mock_response

    client = PylonClient()
    accounts = client.get_accounts()
    assert len(accounts) == 2
    assert accounts[0]['name'] == "account1"

@patch('requests.get')
def test_get_accounts_UnsuccessfulResponse_RaisesPylonException(mock_get, mock_env):
    mock_response = Mock()
    mock_response.status_code = 500
    mock_get.return_value = mock_response

    client = PylonClient()
    with pytest.raises(PylonException):
        client.get_accounts()

@patch('requests.get')
@patch('requests.patch')
def test_update_account_SuccessfulPatch_ReturnsResponse(mock_patch, mock_get, mock_env):
    mock_get_response = Mock()
    mock_get_response.status_code = 200
    mock_get_response.json.return_value = {"data": [{"id": "123", "name": "account1"}]}
    mock_get.return_value = mock_get_response

    mock_patch_response = Mock()
    mock_patch_response.status_code = 200
    mock_patch.return_value = mock_patch_response

    client = PylonClient()
    payload = {"name": "updated_account"}
    response = client.update_account("123", payload)
    assert response.status_code == 200

@patch('requests.get')
def test_get_account_ExistingAccount_ReturnsAccount(mock_get, mock_env):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"data": [{"name": "account1"}]}
    mock_get.return_value = mock_response

    client = PylonClient()
    account = client.get_account("account1")
    assert account['name'] == "account1"

def test_get_account_NonexistentAccount_RaisesPylonException(mock_env):
    client = PylonClient()
    with pytest.raises(PylonException):
        client.get_account("nonexistent_account")

@patch('requests.get')
@patch('requests.patch')
def test_update_account_UnsuccessfulPatch_RaisesHTTPException(mock_patch, mock_get, mock_env):
    mock_get_response = Mock()
    mock_get_response.status_code = 200
    mock_get_response.json.return_value = {"data": [{"id": "123", "name": "account1"}]}
    mock_get.return_value = mock_get_response

    mock_patch_response = Mock()
    mock_patch_response.status_code = 500
    mock_patch.return_value = mock_patch_response

    client = PylonClient()
    payload = {"name": "updated_account"}
    with pytest.raises(HTTPException):
        client.update_account("123", payload)
