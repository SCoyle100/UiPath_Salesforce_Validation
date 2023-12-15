import requests

url = "https://login.salesforce.com/services/oauth2/token"

payload = {
    "grant_type": "password", #keep this the same.  This specifies the type, which is password
    "client_id": "CLIENT ID",
    "client_secret": "CLIENT SECRET",
    "username": "PUT USERNAME HERE",
    "password": "PUT YOUR PASSWORD + SECURITY TOKEN CONCATENATED TOGETHER HERE - NO SPACES"
}

headers = {'Content-Type': 'application/x-www-form-urlencoded'}


response = requests.post(url, data=payload)

print(response.json())
