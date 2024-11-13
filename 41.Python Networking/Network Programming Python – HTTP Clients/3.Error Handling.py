# Import Libraries
import requests

# Error Handling
try:

    # Creating Request
    req = requests.get('https://www.geeksforgeeks.org/', timeout=0.000001)

except requests.exceptions.RequestException as e:

    # Raising Error
    raise SystemExit(e)
