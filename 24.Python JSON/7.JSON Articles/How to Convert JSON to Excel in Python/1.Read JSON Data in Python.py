import json
import pandas as pd

# Load JSON data
with open('data.json') as file:
    data = json.load(file)

print(data)
