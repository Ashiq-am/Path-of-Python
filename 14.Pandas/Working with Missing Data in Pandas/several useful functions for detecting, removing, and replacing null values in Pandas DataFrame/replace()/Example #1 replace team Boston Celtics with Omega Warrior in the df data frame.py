# this will replace "Boston Celtics" with "Omega Warrior"
from pandas.tests.groupby.test_value_counts import df

df.replace(to_replace ="Boston Celtics",
				value ="Omega Warrior")
