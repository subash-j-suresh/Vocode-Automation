import pytest
from unittest.mock import patch, MagicMock
from flask import Flask, jsonify

from error_handler.exception_handlers import webhook_exception_handler

# Create a simple Flask app for testing
app = Flask(__name__)

@app.route('/test', methods=['GET'])
@webhook_exception_handler
def dummy_route():
    return jsonify({"message": "Success!"})

def test_webhook_exception_handler_SuccessfulFunction_ReturnsSuccess():
    with app.test_client() as client:
        with app.app_context():
            response = client.get('/test')
            assert response.status_code == 200
            assert response.json == {"message": "Success!"}