import json
from jsonpath_ng import jsonpath, parse

json_data = '{"name": "John", "age": 25, "city": "", "email": null}'
parsed_json = json.loads(json_data)

# Using select with a lambda function for filtering
jsonpath_expr = parse("$..*").find(parsed_json)
matches = [match.value for match in jsonpath_expr if match.value == '' or match.value is None]
result = bool(matches)

print(f"Does the JSON object have empty values? {result}")
