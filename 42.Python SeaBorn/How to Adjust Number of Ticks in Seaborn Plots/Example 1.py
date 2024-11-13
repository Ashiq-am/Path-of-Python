import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="darkgrid")

# create DataFrame
df = pd.DataFrame({'a': np.random.rand(8), 'b': np.random.rand(8)})

# create lineplot
g = sns.lineplot(data=df)

# set the ticks first
g.set_xticks(range(8))

# set the labels
g.set_xticklabels(['2011', '2012', '2013', '2014',
				'2015', '2016', '2017', '2018'])
