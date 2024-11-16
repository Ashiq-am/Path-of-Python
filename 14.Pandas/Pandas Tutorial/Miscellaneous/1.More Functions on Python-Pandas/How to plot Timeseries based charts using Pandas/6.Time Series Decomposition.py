import statsmodels.api as sm
from pylab import rcParams
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Separating the Date Component into
# Year and Month
dataframe['Date'] = dataframe.index
dataframe['Year'] = dataframe['Date'].dt.year
dataframe['Month'] = dataframe['Date'].dt.month

# using inbuilt style
plt.style.use("fivethirtyeight")

# Creating a dataframe with "Date" and "A"
# columns only. This dataframe is date indexed
decomposition_dataframe = dataframe[['Date', 'A']].copy()
decomposition_dataframe.set_index('Date', inplace=True)
decomposition_dataframe.index = pd.to_datetime(decomposition_dataframe.index)

# using sm.tsa library, we are plotting the
# seasonal decomposition of the "A" column
# Multiplicative Model : Y[t] = T[t] * S[t] * R[t]
decomposition = sm.tsa.seasonal_decompose(decomposition_dataframe,
										model='multiplicative', freq=5)
decomp = decomposition.plot()
decomp.suptitle('"A" Value Decomposition')

# changing the runtime configuration parameters to
# have a desired plot of desired size, etc
rcParams['figure.figsize'] = 12, 10
rcParams['axes.labelsize'] = 12
rcParams['ytick.labelsize'] = 12
rcParams['xtick.labelsize'] = 12
