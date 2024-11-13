# Python code to implement
# the isclose()function

# importing "cmath"
# for mathematical operations
import cmath

# using cmath.isclose() method
val = cmath.isclose(1 + 2j, 1 + 2j, abs_tol=0.5)
print(val)

val1 = cmath.isclose(1 + 2.2j, 1 + 2j, abs_tol=0.5)
print(val1)
