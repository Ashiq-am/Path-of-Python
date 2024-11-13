# import all the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# create a dataframe
Sports = {
	"medals": [100, 98, 102, 56, 78, 56, 78, 96],
	"Time_Period": [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]
}

df = pd.DataFrame(Sports)
print(df)

# to plot the graph
df.plot(x="Time_Period", y="medals", kind="line")
plt.show()
