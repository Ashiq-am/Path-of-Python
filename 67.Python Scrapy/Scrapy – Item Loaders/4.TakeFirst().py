# import the processor module
from itemloaders.processors import TakeFirst

# Create object of TakeFirst processor
proc = TakeFirst()

# assign values and print the result
print(proc(['', 'star','moon','galaxy']))
