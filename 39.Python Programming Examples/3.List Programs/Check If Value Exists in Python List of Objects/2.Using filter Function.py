# Using the filter function to check for the existence of a person with age 30
target_age = 30
filtered_people = filter(lambda person: person.age == target_age, people)
found = any(filtered_people)

if found:
	print(f"A person with age {target_age} exists in the list.")
else:
	print(f"No person with age {target_age} found in the list.")
