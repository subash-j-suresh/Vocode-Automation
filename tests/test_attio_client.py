import os
import pytest
from automation_clients.attio_client import AttioClient

@pytest.fixture
def mock_env():
    # Set up environment variable for tests
    os.environ['ATTIO_API_KEY'] = 'test_api_key'
    yield
    # Clean up environment variable after the test
    del os.environ['ATTIO_API_KEY']

def test_attio_client_initialization(mock_env):
    client = AttioClient()
    assert client.api_key == 'test_api_key'

def test_get_api_key(mock_env):
    api_key = AttioClient.get_api_key()
    assert api_key == 'test_api_key'