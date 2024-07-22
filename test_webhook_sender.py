import requests

deal_data_webhook_url = "http://localhost:5000/webhook/deal_info"
# support_plan_webhook_url = "http://localhost:5000/webhook/support_plan"

# Data to be sent in the POST request
deal_data = {
    "company_name": "Subash_TestCompany",
    "deal_size": "xl",
    "deal_stage": "discovery",
}

# support_plan_data = {"company_name": "Subash_TestCompany", "support_plan": "Free"}

response = requests.post(deal_data_webhook_url, json=deal_data)
# response = requests.post(support_plan_data, json=support_plan_data)

print(f"Response status code: {response.status_code}")
print(f"Response content: {response.content}")
