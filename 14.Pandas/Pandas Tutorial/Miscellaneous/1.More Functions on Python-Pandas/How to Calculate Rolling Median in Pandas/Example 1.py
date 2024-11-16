# Import the `pandas` library
import pandas as pd

# Create the pandas dataframe
df = pd.DataFrame({
	"value": [101, 94, 112, 100, 134, 124,
			119, 127, 143, 128, 141]
})

# Calculate the rolling median for window = 1
w1_roll_median = df.rolling(window=1).median()

# Calculate the rolling median for window = 2
w2_roll_median = df.rolling(window=2).median()

# Calculate the rolling median for window = 3
w3_roll_median = df.rolling(window=3).median()

# Calculate the rolling median for window = 4
w4_roll_median = df.rolling(window=4).median()

# Add the rolling median series to the original
# dataframe for comparison
df['w1_roll_median'] = w1_roll_median
df['w2_roll_median'] = w2_roll_median
df['w3_roll_median'] = w3_roll_median
df['w4_roll_median'] = w4_roll_median

# Print the dataframe
print(df)
