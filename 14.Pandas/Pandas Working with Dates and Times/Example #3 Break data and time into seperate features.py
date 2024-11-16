# Create date and time with dataframe
from turtle import pd

rng = pd.DataFrame()
rng['date'] = pd.date_range('1/1/2011', periods=72, freq='H')

# Print the dates in dd-mm-yy format
rng[:5]

# Create features for year, month, day, hour, and minute
rng['year'] = rng['date'].dt.year
rng['month'] = rng['date'].dt.month
rng['day'] = rng['date'].dt.day
rng['hour'] = rng['date'].dt.hour
rng['minute'] = rng['date'].dt.minute

# Print the dates divided into features
rng.head(3)