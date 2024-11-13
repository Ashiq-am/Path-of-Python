# Python program to demonstrate
# mypy


def sum(a: int, b: int) -> int:
	return a + b

sum( 1, '2') # Argument 2 to "sum" has incompatible type "str"; expected "int"
sum(1, b'2') # Argument 2 to "sum" has incompatible type "bytes"; expected "int"
