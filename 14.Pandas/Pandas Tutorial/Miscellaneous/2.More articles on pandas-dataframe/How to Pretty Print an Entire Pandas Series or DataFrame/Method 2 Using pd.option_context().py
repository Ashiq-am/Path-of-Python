from IPython.core.display import display
from pandas.tests.test_downstream import df
from plotly.express import pd

with pd.option_context('display.max_rows', 5,
					'display.max_columns', None,
					'display.width', 1000,
					'display.precision', 3,
					'display.colheader_justify', 'left'):
	display(df)
