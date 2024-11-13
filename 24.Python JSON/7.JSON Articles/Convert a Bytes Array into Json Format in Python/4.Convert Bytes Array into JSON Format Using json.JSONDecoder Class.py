import json

# Sample complex bytes array
bytes_data = b'{"key": "value", "nested": {"inner_key": [1, 2, 3]}}'

# Custom JSON decoder for more complex scenarios
class ComplexDecoder(json.JSONDecoder):
	def decode(self, s, **kwargs):
		# Implement custom decoding logic if needed
		return super().decode(s, **kwargs)

print(type(bytes_data))
# Decode bytes using the custom decoder
json_data = json.loads(bytes_data, cls=ComplexDecoder)

# Display the resulting JSON data
print(json_data)
print(type(json_data))
