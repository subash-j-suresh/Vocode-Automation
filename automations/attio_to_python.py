from flask import Blueprint, jsonify, request
from automation_clients.pylon_client import PylonClient
from error_handler.automation_exception import AutomationException
from error_handler.error_type import ErrorTypes

attio_deal_modified_wh = Blueprint('attio_to_pylon', __name__)

@attio_deal_modified_wh.route('/webhook', methods=['POST'])
def update_deal_info_to_pylon():
    try:
        attio_data = request.json
        if not attio_data:
            return jsonify({'error': 'Invalid data'}), 400

        pylon_client = PylonClient()
        account = pylon_client.get_account('anotherandomboy@gmail.com')
        if not account:
            return jsonify({'error': 'Account not found'}), 404

        payload = {
            "custom_fields": [
                {"slug": "deal_size", "value": attio_data.get('deal_size')},
                {"slug": "deal_stage", "value": attio_data.get('deal_stage')},
                {"slug": "vocode_plan", "value": attio_data.get('plan_type')}
            ]
        }

        pylon_client.update_account(account['id'], payload)
        
    except AutomationException as e:
        AutomationException.log_error(e)
    except Exception as e:
        exception = AutomationException(-1, ErrorTypes.UNDEFINED_ERROR, str(e))
        AutomationException.log_error(exception)

    return jsonify({'status': 'success'}), 200

@attio_deal_modified_wh.route('/webhook', methods=['POST'])
def update_deal_info_to_pylon():
    try:
        attio_data = request.json
        if not attio_data:
            return jsonify({'error': 'Invalid data'}), 400

        pylon_client = PylonClient()
        account = pylon_client.get_account('anotherandomboy@gmail.com')
        if not account:
            return jsonify({'error': 'Account not found'}), 404

        payload = {
            "custom_fields": [
                {"slug": "vocode_plan", "value": attio_data.get('plan_type')}
            ]
        }

        pylon_client.update_account(account['id'], payload)
        
    except AutomationException as e:
        AutomationException.log_error(e)
    except Exception as e:
        exception = AutomationException(-1, ErrorTypes.UNDEFINED_ERROR, str(e))
        AutomationException.log_error(exception)

    return jsonify({'status': 'success'}), 200