# Importing Math module
import math

# printing whether two values are close or not
print(math.isclose(2.005, 2.125, abs_tol = 0.25))
print(math.isclose(2.547, 2.0048, abs_tol = 0.5))
print(math.isclose(2.0214, 2.00214, abs_tol = 0.02))
