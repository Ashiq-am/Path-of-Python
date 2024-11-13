import requests

# sending a get http request to specified url
response = requests.request(
	"GET", "https://www.geeksforgeeks.org/", verify=False)

# response data
print(response.text)
print(response)
