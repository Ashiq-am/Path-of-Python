import timeit

code_snippets =["""\
try:
	result = 1000 / value
except ZeroDivisionError:
	pass""",
"""\
if value:
	result = 1000 / value""",
]

for value in (1, 0):
	for code in code_snippets:
		t = timeit.Timer(stmt = code, setup ='value ={}'.format(value))
		print("----------------------")
		print("value = {}\n{}".format(value, code))
		print("%.2f usec / pass\n" % (1000000 * t.timeit(number = 100000)/100000))
