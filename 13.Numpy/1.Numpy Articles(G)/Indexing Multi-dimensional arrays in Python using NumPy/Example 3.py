import numpy as np

# here inside arrange method we
# provide start, end, step as
# arguments.
arr_b = np.arrange(20, 30, 2)

# step argument helps in printing
# every said step and skipping the
# rest.
print(arr_b)


print(arr_b[2])

# Slicing operation from index
# 1 to 3
print(arr_b[1:4])
