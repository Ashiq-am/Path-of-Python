# python code to demonstrate working of iteritems(),items()

d = {"geeks": "for", "only": "geeks"}

# using iteritems to print the dictionary key-value pair
print("The key value pair using iteritems is : ")
for i, j in d.iteritems():
    print(i, j)

# using items to print the dictionary key-value pair
print("The key value pair using items is : ")
for i, j in d.items():
    print(i, j)
