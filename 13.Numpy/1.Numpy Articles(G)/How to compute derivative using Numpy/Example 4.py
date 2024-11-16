import numpy as np

# defining polynomial function
var = np.poly1d([3, 5, 4, 9, 5, 1, 6])
print("Polynomial function:\n", var)

# calculating the derivative
derivative = var.deriv()
print("Derivative, f(x)'=\n", derivative)

# calculates the derivative of after
# given value of x
print("When x=1 f(x)'=", derivative(1))
derivative1 = derivative.deriv()

print("\n\nDerivative, f(x)''=\n", derivative1)
print("When x=1 f(x)'=", derivative1(1))
