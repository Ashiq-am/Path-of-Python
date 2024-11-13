''''''





'''There are various other expressions that can be simply coded similar to list comprehensions but instead of 
brackets we use parenthesis. These expressions are designed for situations where the generator is used 
right away by an enclosing function. Generator expression allows creating a generator without a yield keyword. 

However, it doesn’t share the whole power of generator created with a yield function. Example :'''




# Python code to illustrate generator expression
generator = (num ** 2 for num in range(10))
for num in generator:
	print(num)







'''We can also generate a list using generator expressions :'''




string = 'geek'
li = list(string[i] for i in range(len(string)-1, -1, -1))
print(li)
