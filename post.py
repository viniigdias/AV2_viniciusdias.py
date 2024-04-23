import requests

url = "http://127.0.0.1:5000/transaction"
data = {
    "user_id": "user1",
    "password": "pass1",
    "transaction_type": "cash",
    "amount": 100
}

response = requests.post(url, json=data)

print(response.text)