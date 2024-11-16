# Python code explaining
# numpy.pandas.CategoricalDtype()

# importing libraries
import numpy as np
import pandas as pd
from pandas.api.types import CategoricalDtype

a = CategoricalDtype(['a', 'b', 'c'], ordered=True)
print("a : ", a)

b = CategoricalDtype(['a', 'b', 'c'])
print("\nb : ", b)

print("\nTrue / False : ", a == CategoricalDtype(['a', 'b', 'c'],
                                                 ordered=False))

c = pd.api.types.CategoricalDtype(categories=["a", "b", "d", "c"], ordered=True)
print("\nType : ", c)
