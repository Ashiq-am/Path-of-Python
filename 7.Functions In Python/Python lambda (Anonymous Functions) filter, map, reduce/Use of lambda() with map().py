# Python code to illustrate
# map() with lambda()
# to get double of a list.
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
final_list = list(map(lambda x: x*2 , li))
print(final_list)






'''The map() function in Python takes in a function and a list as argument. 
The function is called with a lambda function and a list and 
a new list is returned which contains all the lambda modified items returned by that function for each item'''