import numpy as np
a = np.array([17, 11, 19]) # 1x3 Dimension array
print(a)
b = 3
print(b)

# Broadcasting happened beacuse of
# miss match in array Dimension.
c = a + b
print(c)
