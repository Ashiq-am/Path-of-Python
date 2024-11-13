# loading gc
import gc

# get the current collection
# thresholds as a tuple
print("Garbage collection thresholds:",
					gc.get_threshold())




#Here, the default threshold on the above system is 700.
# This means when the number of allocations vs. the number of deallocations is greater than 700 the automatic garbage collector will run.
# Thus any portion of your code which frees up large blocks of memory is a good candidate for running manual garbage collection.