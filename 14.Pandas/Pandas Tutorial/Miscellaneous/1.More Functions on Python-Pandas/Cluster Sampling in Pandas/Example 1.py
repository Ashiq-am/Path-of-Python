# import pandas
import pandas as pd

# import numpy
import numpy as np

# creating dictionary of data
data = {'N_numbers':np.arange(1,16)}

# creating dataframe
df = pd.DataFrame(data)

# sample of data
samples = df.sample(4)
print(samples)
