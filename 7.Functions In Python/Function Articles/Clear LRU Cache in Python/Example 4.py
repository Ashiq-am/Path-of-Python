import gc
import functools

@functools.lru_cache(maxsize = None)
def gfg():
	# insert function logic here
	pass

@functools.lru_cache(maxsize = None)
def gfg1():
	# insert function logic here
	pass

@functools.lru_cache(maxsize = None)
def gfg2():
	# insert function logic here
	pass

gfg()
gfg1()
gfg2()

gc.collect()

# All objects collected
objects = [i for i in gc.get_objects()
		if isinstance(i, functools._lru_cache_wrapper)]

# All objects cleared
for object in objects:
	object.cache_clear()
