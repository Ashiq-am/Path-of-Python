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

# PRINT THE DATATYPE OF
# EACH COLUMN BEFORE MANUPULATION
print(df.dtypes)


# FUNCTION TO REMOVE TIMEZONE
def remove_timezone(dt):
    # HERE `dt` is a python datetime
    # object that used .replace() method
    return dt.replace(tzinfo=None)


# APPLY THE ABOVE FUNCTION TO
# REMOVE THE TIMEZONE INFORMATION
# FROM EACH RECORD OF TIMESTAMP COLUMN IN DATAFRAME
df['timestamp'] = df['timestamp'].apply(remove_timezone)

# PRINT THE DATATYPE OF
# EACH COLUMN AFTER MANIPULATION
print(df.dtypes)
