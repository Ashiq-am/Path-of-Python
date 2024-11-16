# Python program to
# calculate exponential moving averages
import pandas as pd

arr = [1, 2, 3, 7, 9]

# Convert array of integers to pandas series
numbers_series = pd.Series(arr)

# Get the moving averages of series
# of observations till the current time
moving_averages = round(numbers_series.ewm(
alpha=0.5, adjust=False).mean(), 2)

# Convert pandas series back to list
moving_averages_list = moving_averages.tolist()

print(moving_averages_list)
