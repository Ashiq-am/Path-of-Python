# make a post request
response = requests.request("POST", url, data = my_data,headers = headers)
#load json data from source
returned_msg = json.loads(response.text)

# print the send message
print(returned_msg['message'])
