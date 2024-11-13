from functools import singledispatch

@singledispatch
def geek_func(arg):
	print("Function Call with single argument")

@geek_func.register(int)
def _(arg):
	print("Function Called with an integer")

@geek_func.register(str)
def _(arg):
	print("Function Called with a string")

@geek_func.register(list)
def _(arg):
	print("Function Called with a list")

geek_func(1)
geek_func([1, 2, 3])
geek_func("geek")
geek_func({1: "geek1", 2: "geek2"})
