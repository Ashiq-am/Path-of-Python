import statsmodels.api as sm
from statsmodels.formula.api import ols
import pandas as pd

data = sm.datasets.get_rdataset("PlantGrowth").data
