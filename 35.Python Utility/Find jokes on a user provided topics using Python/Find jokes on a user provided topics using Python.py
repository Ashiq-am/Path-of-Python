import requests
import pyfiglet
import termcolor
from random import choice

header = pyfiglet.figlet_format("Find a joke!")
header = termcolor.colored(header, color="white")
print(header)

term = input("Let me tell you a joke! Give me a topic: ")

response_json = requests.get("https://icanhazdadjoke.com/search",headers={"Accept": "application/json"}, params={"term": term}).json()

results = response_json["results"]

total_jokes = response_json["total_jokes"]
print(total_jokes)

if total_jokes > 1:
	print(f"I've got {total_jokes} jokes about {term}. Here's one:\n", choice(
		results)['joke'])

elif total_jokes == 1:
	print(f"I've got one joke about {term}. Here it is:\n", results[0]['joke'])

else:
	print(f"Sorry, I don't have any jokes about {term}! Please try again.")
