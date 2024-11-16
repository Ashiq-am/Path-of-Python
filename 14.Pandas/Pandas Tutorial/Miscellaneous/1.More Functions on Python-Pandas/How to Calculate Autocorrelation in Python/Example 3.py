# import thr required modules
import pandas as pd
from statsmodels.graphics.tsaplots import plot_acf

# read the csv data
data = pd.read_csv("daily-minimum-temperatures-in-blr.csv",
				header=0, index_col=0, parse_dates=True,
				squeeze=True)

# plot the auto correlaion
plot_acf(data)
