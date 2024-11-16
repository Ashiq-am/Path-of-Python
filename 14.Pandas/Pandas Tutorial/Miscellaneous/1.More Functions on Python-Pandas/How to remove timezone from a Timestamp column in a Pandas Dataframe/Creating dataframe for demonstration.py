import pandas as pd
from datetime import datetime, timezone

# CREATE THE PANDAS DATAFRAME
# WITH TIMESTAMP COLUMN
df = pd.DataFrame({
	"orderNo": [
		"4278954",
		"3473895",
		"8763762",
		"4738289",
		"1294394"
	],
	"timestamp": [
		datetime.strptime("2021-06-01",
						"%Y-%m-%d").replace(tzinfo=timezone.utc),
		datetime.strptime("2021-06-02",
						"%Y-%m-%d").replace(tzinfo=timezone.utc),
		datetime.strptime("2021-06-03",
						"%Y-%m-%d").replace(tzinfo=timezone.utc),
		datetime.strptime("2021-06-04",
						"%Y-%m-%d").replace(tzinfo=timezone.utc),
		datetime.strptime("2021-06-05",
						"%Y-%m-%d").replace(tzinfo=timezone.utc)
	]
})

# PRINT THE DATATYPES OF
# EACH COLUMN OF DATAFRAME
print(df.dtypes)

# VIEW THE DATAFRAME
print(df)
