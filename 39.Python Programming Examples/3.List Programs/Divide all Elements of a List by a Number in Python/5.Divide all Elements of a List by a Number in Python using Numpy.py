import numpy as np

# Same list as the one used in the previous example
l = [14, 8, 0, 12, 981, 21, -99]

arr = np.array(l)

divisor = 7
res = (arr//divisor).tolist()

divisor2 = 10
res2 = np.divide(arr, divisor2)

print(res)
print(res2)
