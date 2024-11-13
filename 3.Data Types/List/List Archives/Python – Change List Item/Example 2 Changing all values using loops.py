# list
list = [10, 20, 30, 40, 50, 60]
print("Original list ")
print(list)

print("After incrementing each element of list by 2")

# adding 2 to each value of list
# len method to calculate length of list
# range method is used to go upto a certain range
for i in range(len(list)):
    list[i] = list[i] + 2

print(list)
