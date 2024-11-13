# Import required processors
from itemloaders.processors import Join

# Put separator <br> while creating Join() object
proc = Join('<a>')

# pass the values and print result
print(proc(['Sky', 'Moon','Stars']))
