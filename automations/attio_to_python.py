from flask import Blueprint, jsonify, request
from automation_clients.pylon_client import PylonClient
from error_handler.exception_handlers import webhook_exception_handler

attio_deal_modified_wh = Blueprint("attio_to_pylon", __name__)


@attio_deal_modified_wh.route("/webhook", methods=["POST"])
@webhook_exception_handler
def update_deal_info_to_pylon():
    attio_data = request.json
    if not attio_data:
        return jsonify({"error": "Invalid data"}), 400

    company_name = attio_data.get("company_name")
    pylon_client = PylonClient()
    account = pylon_client.get_account(company_name)

    payload = {
        "custom_fields": [
            {"slug": "deal_size", "value": attio_data.get("deal_size")},
            {"slug": "deal_stage", "value": attio_data.get("deal_stage")},
        ]
    }

    pylon_client.update_account(account["id"], payload)
    return jsonify({"status": "success"}), 200


@attio_deal_modified_wh.route("/webhook1", methods=["POST"])
@webhook_exception_handler
def update_support_plan_info_to_pylon():
    attio_data = request.json
    if not attio_data:
        return jsonify({"error": "Invalid data"}), 400

    company_name = attio_data.get("company_name")
    pylon_client = PylonClient()
    account = pylon_client.get_account(company_name)

    payload = {
        "custom_fields": [
            {"slug": "support_plan", "value": attio_data.get("support_plan")}
        ]
    }

    pylon_client.update_account(account["id"], payload)

    return jsonify({"status": "success"}), 200
