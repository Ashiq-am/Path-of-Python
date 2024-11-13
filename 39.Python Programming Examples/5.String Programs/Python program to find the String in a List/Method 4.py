# assign list
l = ['hello', 'geek', 'have', 'a', 'geeky', 'day']

# assign string
s = 'prime'

# check if string is present in list
if any(s in i for i in l):
	print(f'{s} is present in the list')
else:
	print(f'{s} is not present in the list')
