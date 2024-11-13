# Sample dictionary
grades = {'Alice': 90, 'Bob': 85, 'Charlie': 92, 'David': 78}

# Iterating with a custom start index
for position, (student, score) in enumerate(grades.items(), start=1):
	print(f"Position: {position}, Student: {student}, Score: {score}")
