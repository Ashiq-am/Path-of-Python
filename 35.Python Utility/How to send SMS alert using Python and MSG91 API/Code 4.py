# importing the module
import http.client as ht

# establishing connection
conn = ht.HTTPSConnection("api.msg91.com")

# determining the payload
payload = '''{"sender": "MSGAPI", 
			"route": "4", 
			"country": "91", 
			"sms": [ 
				{ 
				"message": "Welcome GeeksForGeeks, Today you have PC class", 
				"to": [ 
					"9090XX8921" 
				] 
				}, 
			] 
			}'''

# creating the header
headers = {
	'authkey': "",
	'content-type': "application / json"
}

# sending the connection request
conn.request("POST", "/api / v2 / sendsms", payload, headers)

res = conn.getresponse()
data = res.read()

# printing the acknowledgement
print(data.decode("utf-8"))
