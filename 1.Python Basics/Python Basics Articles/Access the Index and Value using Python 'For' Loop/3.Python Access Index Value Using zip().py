# Method 3: Using zip
# create a index list that stores list
indexlist = [0, 1, 2, 3]

# create a list of fruits
fruits = ['apple', 'banana', 'orange']

print("index and values in list:")

# get the values from indices using zip method
for index, value in zip(indexlist, fruits):
    print(index, value)
