# Python3 code to demonstrate
# Dictionary key transcription
# dictionary comprehension

# initializing list
test_list = [{'state' : 'Haryana', 'capital' : 'Chandigarh', 'area' : 'North'},
			{'state' : 'Karnataka', 'capital' : 'Bengaluru', 'area' : 'South'}]

# printing original list
print("The original list : " + str(test_list))

# using Dictionary comprehension
# Dictionary key transcription
res = { sub["state"]: {"capital": sub["capital"], "area": sub["area"] }
		for sub in test_list }

# print result
print("The Dictionary after transcription of key : " + str(res))
