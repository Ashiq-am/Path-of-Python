# create a list with 7 integer elements
data=[11,23,13,3,1,3,4]

# use list comprehension to get square
# of odd numbers
result = [i*i for i in data if i%2!=0]

# display the result
print(result)
