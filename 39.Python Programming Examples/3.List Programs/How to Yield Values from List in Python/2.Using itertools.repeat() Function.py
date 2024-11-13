from itertools import repeat

def yield_using_repeat(lst, repeat_count):
	for item in repeat(lst, repeat_count):
		yield from item

data = ["Python", "Java", "C++", "JavaScript", "HTML", "CSS"]
repeat_count = 1

for language in yield_using_repeat(data, repeat_count):
	print(language)
