# Import Libraries
import requests

# Creating Session
s = requests.Session()
s.get('http://httpbin.org/cookies/set/sessioncookie/419735271')

# Getting Response
r = s.get('http://httpbin.org/cookies')

# Show Response
print(r.text)
