# importing required module
import urllib.parse
import requests

# setting the base URL value
baseUrl = "https://v6.exchangerate-api.com/v6/0f215802f0c83392e64ee40d/pair/"

First = input("Enter First Currency Value")
Second = input("Enter Second Currency Value")

result = First+"/"+Second
final_url = baseUrl+result

# retreiving data from JSON Data
json_data = requests.get(final_url).json()
Final_result = json_data['conversion_rate']

print("Conversion rate from "+First+" to "+Second+" = ", Final_result)
