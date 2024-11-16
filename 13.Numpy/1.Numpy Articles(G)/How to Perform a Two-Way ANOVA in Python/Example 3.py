# Importing libraries
import statsmodels.api as sm
from statsmodels.formula.api import ols

# Performing two-way ANOVA
model = ols(
	'height ~ C(Fertilizer) + C(Watering) +\
	C(Fertilizer):C(Watering)', data=df).fit()
sm.stats.anova_lm(model, typ=2)
