import numpy as np

l1 =[5, 7, 10, 14, 19, 25, 32]
print("Result 1: ", np.unwrap(l1, discont = 4))

l2 =[0, 1.34237486723, 4.3453455, 8.134654756, 9.3465456542]
print("Result 2: ", np.unwrap(l2, discont = 3.1))
