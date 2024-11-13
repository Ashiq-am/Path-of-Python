# f function to evaluate expression
def exp_eval(a, b):
	ans = (a*a)+(3*(b*b))+(a*b)
	return ans


# values to be evaluated
a = 2
b = 4

# formatting
print(f"The expression a**2+3b**2+(a*b) = {exp_eval(a,b)}")
