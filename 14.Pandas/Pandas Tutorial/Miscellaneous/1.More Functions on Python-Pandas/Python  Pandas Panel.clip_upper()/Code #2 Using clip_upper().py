# creating an empty panel
import pandas as pd
import numpy as np

data = {'Item1': pd.DataFrame(np.random.randn(7, 4)),
        'Item2': pd.DataFrame(np.random.randn(4, 5))}

pen = pd.Panel(data)
print(pen['Item1'], '\n')

p = pen['Item1'][0].clip_upper(np.random.randn(7))
print(p)
