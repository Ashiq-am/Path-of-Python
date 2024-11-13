import statsmodels.api as sm
from statsmodels.formula.api import ols
import pandas as pd

# Example dataset
data = sm.datasets.get_rdataset("Moore", "carData").data
data = data.rename(columns={"partner.status": "partner_status"})
