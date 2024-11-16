# Program to calculate cumulative moving average
# using numpy

import numpy as np

arr = [1, 2, 3, 7, 9]

i = 1
# Initialize an empty list to store cumulative moving
# averages
moving_averages = []

# Store cumulative sums of array in cum_sum array
cum_sum = np.cumsum(arr);

# Loop through the array elements
while i <= len(arr):
    # Calculate the cumulative average by dividing
    # cumulative sum by number of elements till
    # that position
    window_average = round(cum_sum[i - 1] / i, 2)

    # Store the cumulative average of
    # current window in moving average list
    moving_averages.append(window_average)

    # Shift window to right by one position
    i += 1

print(moving_averages)
