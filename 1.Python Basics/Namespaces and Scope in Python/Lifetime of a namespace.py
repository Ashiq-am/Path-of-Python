# var1 is in the global namespace
var1 = 5
def some_func():

	# var2 is in the local namespace
	var2 = 6
	def some_inner_func():

		# var3 is in the nested local
		# namespace
		var3 = 7







'''As shown in the following figure, same object name can be present in multiple namespaces as isolation between the 
same name is maintained by their namespace.'''







"""But in some cases, one might be interested in updating or processing global variable only, as shown in the following 
example, one should mark it explicitly as global and the update or process."""






# Python program processing
# global variable

count = 5
def some_method():
	global count
	count = count + 1
	print(count)
some_method()
