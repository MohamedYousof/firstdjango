import requests

url = "https://developer-api.bringg.com/partner_api/customers"

querystring = {"company_id": "11023", "access_token": "jsFutZFDa71G7Kfz9zrG"}

response = requests.request(method="GET", url=url, params=querystring)
print(response)
print(response.text)
