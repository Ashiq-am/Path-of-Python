# Import the processor module
from itemloaders.processors import Compose

# Create an object of Compose processor and pass values
proc = Compose(lambda v: v[0], str.upper)

# Assign values and print result
print(proc(['hi', 'there']))
