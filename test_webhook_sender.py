import requests

# Your local webhook URL
webhook_url = "http://localhost:5000/webhook"

# Data to be sent in the POST request
data = {"company_name": "xyz", "deal_size": "xl", "deal_stage": "discovery"}

data = {"company_name": "xyz", "support_plan": "Community"}

# Send the POST request to the webhook URL
response = requests.post(webhook_url, json=data)

# Print the response status code and response content
print(f"Response status code: {response.status_code}")
print(f"Response content: {response.content}")
