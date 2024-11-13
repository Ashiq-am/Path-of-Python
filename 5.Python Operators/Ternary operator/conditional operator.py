# Program to demonstrate conditional operator
a, b = 10, 20

# If a is less than b, then a is assigned
# else b is assigned (Note : it doesn't
# work if a is 0.
min = a < b and a or b

print(min)






"""Note : The only drawback of this method is that on_true must not be zero or False. 
If this happens on_false will be evaluated always. The reason for that is if expression is true, 
the interpreter will check for the on_true, if that will be zero or false, 

that will force the interpreter to check for on_false to give the final result of whole expression."""