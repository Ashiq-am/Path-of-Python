generator_data = (x for x in range(5))
print(type(generator_data))

dictionary_result = {}
for item in generator_data:
	dictionary_result[item] = item
print(dictionary_result)
print(type(dictionary_result))
