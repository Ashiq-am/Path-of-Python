import pandas as pd
from plotnine import *


# load dataset
dataset = pd.read_csv("dataset.csv")

(ggplot(dataset, aes(x = "area_0", y = "area_1"))+
	geom_point(color = "label", alpha = 0.7,
			size = 0.5)
)
