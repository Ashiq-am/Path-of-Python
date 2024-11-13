import scipy

# Area of a circle using
# scipy.constants.pi
def Area_of_Circle(r):
	return scipy.constants.pi * r * r

# Calculates the gravational for
def force_gravity(M, m, dist):
	return (scipy.constants.G*M*m) / (dist**2)


print(f'Area of Circle: {Area_of_Circle(5)}')
print(f'Gravitational force: {force_gravity(10,5,1)}')
