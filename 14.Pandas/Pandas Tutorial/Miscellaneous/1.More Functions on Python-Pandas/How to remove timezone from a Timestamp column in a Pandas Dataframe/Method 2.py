import pandas as pd
from datetime import datetime, timezone

# CREATE THE DATAFRAME
df = pd.DataFrame({
	"orderNo": [
		"4278954",
		"3473895",
		"8763762",
		"4738289",
		"1294394"
	],
	"timestamp": [
		datetime.strptime(
			"2021-06-01", "%Y-%m-%d").replace(tzinfo=timezone.utc),
		datetime.strptime(
			"2021-06-02", "%Y-%m-%d").replace(tzinfo=timezone.utc),
		datetime.strptime(
			"2021-06-03", "%Y-%m-%d").replace(tzinfo=timezone.utc),
		datetime.strptime(
			"2021-06-04", "%Y-%m-%d").replace(tzinfo=timezone.utc),
		datetime.strptime(
			"2021-06-05", "%Y-%m-%d").replace(tzinfo=timezone.utc)
	]
})

# PRINT THE DATATYPE OF EACH COLUMN BEFORE
# MANUPULATION
print(df.dtypes)

# REMOVING THE TIMEZONE INFORMATION
df['timestamp'] = df['timestamp'].dt.tz_localize(None)

# PRINT THE DATATYPE OF EACH COLUMN AFTER
# MANIPULATION
print(df.dtypes)
