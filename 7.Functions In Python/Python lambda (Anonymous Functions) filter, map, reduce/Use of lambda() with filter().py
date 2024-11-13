# Python code to illustrate
# filter() with lambda()
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
final_list = list(filter(lambda x: (x%2 != 0) , li))
print(final_list)





"""The filter() function in Python takes in a function and a list as arguments. 
This offers an elegant way to filter out all the elements of a sequence “sequence”, 
for which the function returns True. Here is a small program that returns the odd numbers from an input list:"""