import requests

url = "https://api.github.com/rate_limit"
headers = {"Accept": "application/vnd.github.v3+json"} 
req  = requests.get(url , headers=headers)
print(f"status code: {req.status_code}")


# Convert the response object to a dictionary.
response_dict = req.json()
# print(response_dict)
response_dict = response_dict['resources']

print(f"Request Limit: {response_dict['core']['limit']}")
print(f"Remaining Request / Min : {response_dict['core']['remaining']}")
print(f"Unix Time Left : {response_dict['core']['reset']}")