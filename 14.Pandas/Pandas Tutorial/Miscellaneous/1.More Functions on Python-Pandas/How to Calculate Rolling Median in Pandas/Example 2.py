# Import the `pandas` library
import pandas as pd

# Create the pandas dataframe
df = pd.DataFrame({
	"value": [
		506.40, 487.85, 484.90, 489.70, 501.40, 509.65, 510.75,
		503.45, 507.05, 505.45, 519.05, 530.15, 509.70, 486.10,
		495.50, 488.65, 492.75, 460.20, 461.45, 458.60, 475.25,
	]
})

# Calculate the rolling median for window = 7
w7_roll_median = df.rolling(window=7).median()

# Add the rolling median series to the original
# dataframe for comparison
df['w7_roll_median'] = w7_roll_median

# Print the dataframe
print(df)
