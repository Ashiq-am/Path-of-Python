# Replace Values in a List using Lambda Function

# define list
l = ['Hardik', 'Rohit', 'Rahul', 'Virat', 'Pant']

# replace Pant with Ishan
l = list(map(lambda x: x.replace('Pant', 'Ishan'), l))

# print list
print(l)
