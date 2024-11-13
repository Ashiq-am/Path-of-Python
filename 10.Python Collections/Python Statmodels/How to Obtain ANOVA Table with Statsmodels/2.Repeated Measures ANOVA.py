import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.anova import AnovaRM

data = {
    'subject': ['S1', 'S1', 'S1', 'S2', 'S2', 'S2', 'S3', 'S3', 'S3', 'S4', 'S4', 'S4'],
    'condition': ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C'],
    'reaction_time': [10, 12, 14, 8, 9, 11, 14, 15, 16, 7, 9, 10]
}

df = pd.DataFrame(data)

# Perform Repeated Measures ANOVA
aovrm = AnovaRM(df, 'reaction_time', 'subject', within=['condition'])
res = aovrm.fit()
print(res.summary())
