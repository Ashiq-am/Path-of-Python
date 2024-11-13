# create a list with 7 integer elements
data=[1,2,3,4,5,6,7]

# use list comprehension to get square
# of odd numbers
result = [i*i for i in data if i%2!=0]

# display the result
print(result)
