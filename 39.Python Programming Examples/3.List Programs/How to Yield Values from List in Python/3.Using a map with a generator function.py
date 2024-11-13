def yield_values_generator(lst):
	for item in lst:
		yield item

data = ["Python", "Java", "C++", "JavaScript", "HTML", "CSS"]

generator_result = map(lambda x: x, yield_values_generator(data))

for language in generator_result:
	print(language)
