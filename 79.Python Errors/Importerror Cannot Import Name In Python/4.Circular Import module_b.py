# module_b.py
def function_b():
	from module_a import function_a
	print("Function B")
	function_a()

function_b()
