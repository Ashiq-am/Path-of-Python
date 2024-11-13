import requests as r

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}

response = r.get('http://httpbin.org/headers', headers=headers)

print("The Status Code", response.status_code)
print("The Response Text", response.text)
