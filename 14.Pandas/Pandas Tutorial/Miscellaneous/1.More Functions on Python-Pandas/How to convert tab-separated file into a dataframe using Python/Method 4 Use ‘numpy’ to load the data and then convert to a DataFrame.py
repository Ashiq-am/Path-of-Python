import numpy as np
import pandas as pd
data = np.genfromtxt('file.tsv', delimiter='\t', dtype=None, encoding=None)
df = pd.DataFrame(data)
df.head()
