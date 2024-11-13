import json
from decimal import Decimal

# Decimal object
decimal_number = Decimal('123.456')

# Custom JSON Encoder class

class DecimalEncoder(json.JSONEncoder):
	def default(self, obj):
		if isinstance(obj, Decimal):
			return str(obj)
		return super().default(obj)

# Serialize the Decimal object using custom JSON encoder
json_data = json.dumps(decimal_number, cls=DecimalEncoder)
print(type(decimal_number))
print(type(json_data))
print(json_data)
