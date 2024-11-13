import json
from decimal import Decimal

# Decimal object
decimal_number = Decimal('123.456')
# Define a custom serialization function

def decimal_serializer(obj):
	if isinstance(obj, Decimal):
		return str(obj)
	raise TypeError("Type not serializable")

# Serialize the Decimal object using custom serializer
json_data = json.dumps(decimal_number, default=decimal_serializer)
print(type(decimal_number))
print(type(json_data))
print(json_data)
