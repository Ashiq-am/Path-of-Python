import json
import orjson
import time

# Load JSON data from file
with open('countries.json') as f:
    data = json.load(f)

# Measure the time taken to decode the JSON data using json.loads()
start_time = time.time()
decoded_data_json = json.loads(json.dumps(data))
end_time = time.time()
print(
    f"Time taken to decode JSON data using json.loads(): {end_time - start_time:.4f} seconds")

# Measure the time taken to decode the JSON data using orjson.loads()
start_time = time.time()
decoded_data_orjson = orjson.loads(orjson.dumps(data))
end_time = time.time()
print(
    f"Time taken to decode JSON data using orjson.loads(): {end_time - start_time:.4f} seconds")

# Check if the decoded data is the same for both methods
print(f"Decoded data is the same: {decoded_data_json == decoded_data_orjson}")