# Create a Pandas Timestamp object
ts =pd.Timestamp(year=2024, month=1, day=28, hour=15, minute=30, second=0, microsecond=0)

# Convert the Timestamp to a Python datetime object
datetime_obj = ts.to_pydatetime()

print(datetime_obj)
print(type(datetime_obj))
