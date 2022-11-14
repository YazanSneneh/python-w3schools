import requests
response = requests.get("https://api.kanye.rest/")

print(response.status_code)
# print(dir(requests.Request))
