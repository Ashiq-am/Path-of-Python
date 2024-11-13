''''''






'''When a for loop is executed, for statement calls iter() on the object, which it is supposed to loop over. 
If this call is successful, the iter call will return an iterator object that defines the method __next__(), 
which accesses elements of the object one at a time. The __next__() method will raise a StopIteration exception, 
if there are no further elements available. 

The for loop will terminate as soon as it catches a StopIteration exception.

Let’s call the __next__() method using the next() built-in function.

Function ‘iterable’ will return True, if the object ‘obj’ is an iterable and False otherwise.

'''





# list of cities
cities = ["Berlin", "Vienna", "Zurich"]

# initialize the object
iterator_obj = iter(cities)

print(next(iterator_obj))
print(next(iterator_obj))
print(next(iterator_obj))





"""Note: If ‘next(iterator_obj)’ is called one more time, it would return ‘StopIteration’.
 """



