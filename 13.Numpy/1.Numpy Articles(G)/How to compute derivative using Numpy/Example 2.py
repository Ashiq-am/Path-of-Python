import numpy as np

# defining polynomial function
var = np.poly1d([4, 9, 5, 1, 6])
print("Polynomial function, f(x):\n", var)

# calculating the derivative
derivative = var.deriv()
print("Derivative, f(x)'=\n", derivative)

# calculates the derivative of after
# given value of x
print("When x=3 f(x)'=", derivative(3))
