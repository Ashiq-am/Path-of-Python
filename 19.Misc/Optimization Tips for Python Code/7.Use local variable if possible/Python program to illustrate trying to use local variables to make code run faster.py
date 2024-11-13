# Python program to illustrate trying
# to use local variables to make code
# run faster
class Test:
	def func(self,x):
		print(x+x)

# Declaring variable that assigns class method object
Obj = Test()
mytest = Obj.func # Declaring local variable
n = 2
for i in range(n):
	mytest(i) # faster than Obj.func(i)
