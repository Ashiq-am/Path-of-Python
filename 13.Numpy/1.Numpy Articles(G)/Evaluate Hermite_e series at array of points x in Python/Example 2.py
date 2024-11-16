from numpy.polynomial import hermite_e as H

coef = [3, 5, 7]
print("Result 1 : \n",H.hermeval(1, coef))

x = [[2, 3], [5, 6]]
print("Result 2 : \n",H.hermeval(x, coef))
