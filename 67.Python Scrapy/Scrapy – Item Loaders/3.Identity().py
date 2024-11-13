# Import the processor
from itemloaders.processors import Identity

# Create object of Identity processor
proc = Identity()

# Assign values and print result
print(proc(['star','moon','galaxy']))
