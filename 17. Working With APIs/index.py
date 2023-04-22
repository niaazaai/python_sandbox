import requests

url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"} 

req  = requests.get(url , headers=headers)
print(f"status code: {req.status_code}")


# Convert the response object to a dictionary.
response_dict = req.json()
# print(response_dict)


# Process results.
# print(response_dict.keys())

# get on one key element 
# print(response_dict.items)

# for key , value in response_dict.items():
#     print (f"{key} :::> {value}")

# to go through items element in response api 
# for key , value in response_dict.items():
#     if(key == 'items'):
#         for k  in value:
#             print(f"{k} \n\n\n")


# print(response_dict['items'][0])


# Examine the first repository.
# repo_dict = response_dict['items'][0]
# print(f"\nKeys: {len(repo_dict)}")
# for key in sorted(repo_dict.keys()):
#     print(key)


# repo_dict = response_dict['items'][0]
# print("\nSelected information about first repository:")
# print(f"Name: {repo_dict['name']}")
# print(f"Owner: {repo_dict['owner']['login']}")
# print(f"Stars: {repo_dict['stargazers_count']}")
# print(f"Repository: {repo_dict['html_url']}")
# print(f"Created: {repo_dict['created_at']}")
# print(f"Updated: {repo_dict['updated_at']}")
# print(f"Description: {repo_dict['description']}")


print("\nSelected information about each repository:")
for repo_dict in response_dict['items']:
    print(f"\nName: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Description: {repo_dict['description']}")

