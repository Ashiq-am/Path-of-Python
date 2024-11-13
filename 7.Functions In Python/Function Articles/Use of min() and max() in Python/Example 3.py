# Python code explaining min() and max()
def fun(element):
	return(len(element))

l =["ab", "abc", "bc", "c"]
print(max(l, key = fun))

# you can also write in this form
print(max(l, key = lambda element:len(element)))
