# importing libraries
import numpy as np
import pandas as pd
from pandas.api.types import CategoricalDtype

labels, uniques = pd.factorize(['b', 'd', 'd', 'c', 'a', 'c', 'a', 'b'])

print("Numeric Representation : \n", labels)
print("Unique Values : \n", uniques)
