# assign list
l = ['hello', 'geek', 'have', 'a', 'geeky', 'day']

# assign string
s = 'geek'

# list comprehension
compre = [i for i in l if s in l]

# check if sting is present in list
if len(compre) > 0:
	print(f'{s} is present in the list')
else:
	print(f'{s} is not present in the list')
