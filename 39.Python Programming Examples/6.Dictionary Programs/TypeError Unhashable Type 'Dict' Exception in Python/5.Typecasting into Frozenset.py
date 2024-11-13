temp = {'age': 24}

#typecasting into frozenset
key = frozenset(temp.items())
my_dict = {"name": "shraman",key:'DOB'}
print("Dictionary is : ",my_dict)

# accessing the element
print("Element is : ",my_dict[key])
