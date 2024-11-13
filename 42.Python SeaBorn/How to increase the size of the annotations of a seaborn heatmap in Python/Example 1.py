# Importing Required Libraries
import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as mtb

data = pd.read_csv("bestsellers.csv")

sb.heatmap(data.corr(), annot=True, annot_kws={'size': 15})

mtb.show()
