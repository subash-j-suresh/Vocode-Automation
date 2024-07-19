from quart import Blueprint, request, jsonify
from exception_manager.exception_handlers import webhook_exception_handler
from webhook_manager.webhook_handler_registry import get_handler

webhook_listener = Blueprint("webhook_listener", __name__)


def validate_payload(payload, expected_keys):
    return all(key in payload for key in expected_keys)


async def process_webhook(payload, handler):
    await handler(payload)


@webhook_listener.route("/webhook/<endpoint>", methods=["POST"])
@webhook_exception_handler
async def unified_webhook_listener(endpoint):
    try:
        payload = await request.json
    except Exception:
        return jsonify({"error": "Invalid JSON"}), 400

    handler_info = get_handler(endpoint)
    if handler_info:
        handler, expected_keys = handler_info

        if not validate_payload(payload, expected_keys):
            return jsonify({"error": "Invalid payload structure"}), 400

        response = jsonify({"status": "acknowledged"})
        response.status_code = 200

        # Process the webhook asynchronously
        await process_webhook(payload, handler)

        return response

    return jsonify({"error": "Invalid webhook endpoint"}), 400
