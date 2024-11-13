# import gc module
import gc


# define a function
def geek(name):
	print(name + " - Hello Geek!")


# call the function with names as
# parameter
geek("sravan")
geek("bobby")
geek("ojaswi")
geek("rohith")
geek("gnanesh")

# get all the initialized objects
gc.get_objects()
