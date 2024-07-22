from automation_clients.pylon_client import PylonClient
from webhook_manager.webhook_handler_registry import register_webhook_handler


@register_webhook_handler(
    endpoint="deal_info", expected_keys=["company_name", "deal_size", "deal_stage"]
)
async def update_deal_info_to_pylon(webhook_payload):
    company_name = webhook_payload.get("company_name").strip()
    pylon_client = PylonClient()
    account = pylon_client.get_account(company_name)

    payload = {
        "custom_fields": [
            {"slug": "deal_size", "value": webhook_payload.get("deal_size").lower().strip()},
            {"slug": "deal_stage", "value": webhook_payload.get("deal_stage").lower().strip()},
        ]
    }

    pylon_client.update_account(account["id"], payload)


@register_webhook_handler(
    endpoint="support_plan", expected_keys=["company_name", "support_plan"]
)
async def update_support_plan_info_to_pylon(webhook_payload):
    company_name = webhook_payload.get("company_name")
    pylon_client = PylonClient()
    account = pylon_client.get_account(company_name)

    payload = {
        "custom_fields": [
            {
                "slug": "support_plan",
                "value": webhook_payload.get("support_plan").lower().strip(),
            }
        ]
    }

    pylon_client.update_account(account["id"], payload)
