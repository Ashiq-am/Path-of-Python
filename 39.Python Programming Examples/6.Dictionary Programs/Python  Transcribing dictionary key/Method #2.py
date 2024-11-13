# Python3 code to demonstrate
# Dictionary key transcription
# dictionary comprehension + items() + get()

# initializing list
test_list = [{'state' : 'Haryana', 'capital' : 'Chandigarh', 'area' : 'North'},
			{'state' : 'Karnataka', 'capital' : 'Bengaluru', 'area' : 'South'}]

# printing original list
print("The original list : " + str(test_list))

# using dictionary comprehension + items() + get()
# Dictionary key transcription
res = {sub.get('state'): {key: val for key, val in sub.items()
		if key != 'state'} for sub in test_list}

# print result
print("The Dictionary after transcription of key : " + str(res))
