import orjson

s = '{"India": "Delhi", "Russia": "Moscow", "Japan": "Tokyo"}'

data = orjson.loads(s)
print(data)
