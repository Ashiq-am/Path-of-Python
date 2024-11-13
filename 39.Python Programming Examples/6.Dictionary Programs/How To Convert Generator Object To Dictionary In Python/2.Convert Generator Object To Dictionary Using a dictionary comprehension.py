generator_data = (x for x in range(5))
print(type(generator_data))

dictionary_result = {item: item for item in generator_data}
print(dictionary_result)
print(type(dictionary_result))
