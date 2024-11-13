import numdifftools as nd


g = lambda x:(x**4)+x + 1
grad1 = nd.Gradient(g)([1])
print("Gradient of x ^ 4 + x+1 at x = 1 is ", grad1)

def rosen(x):
	return (1-x[0])**2 +(x[1]-x[0]**2)**2

grad2 = nd.Gradient(rosen)([1, 2])
print("Gradient of (1-x ^ 2)+(y-x ^ 2)^2 at (1, 2) is ", grad2)
