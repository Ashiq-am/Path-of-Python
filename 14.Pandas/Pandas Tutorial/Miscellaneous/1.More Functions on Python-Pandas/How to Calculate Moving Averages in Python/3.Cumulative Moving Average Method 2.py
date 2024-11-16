# Python program to calculate
# cumulative moving averages using pandas
import pandas as pd

arr = [1, 2, 3, 7, 9]
window_size = 3

# Convert array of integers to pandas series
numbers_series = pd.Series(arr)

# Get the window of series of
# observations till the current time
windows = numbers_series.expanding()

# Create a series of moving averages of each window
moving_averages = windows.mean()

# Convert pandas series back to list
moving_averages_list = moving_averages.tolist()

print(moving_averages_list)
