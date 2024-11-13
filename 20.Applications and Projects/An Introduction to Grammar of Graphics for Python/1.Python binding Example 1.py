import pandas as pd
from plotnine import *


# load dataset
dataset = pd.read_csv("dataset.csv")

# ggplot is to plot the given data
(ggplot(dataset, aes(x = "area_0", y = "area_1"))+
	geom_point()
)

# aes contains parameters which work
# as x-axis and y-axis for the given plot
# geom.point() makes the data entries as points
