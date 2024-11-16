# import DataFrame
import pandas as pd

# using DataFrame.dot() method
gfg1 = pd.DataFrame([[1, 4], [9, 5]])
gfg2 = pd.DataFrame([[4, 3, 2, 1], [21, -3, -4, 1]])

print(gfg1.dot(gfg2))
