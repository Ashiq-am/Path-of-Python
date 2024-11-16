# Apply the lambda function to
# capitalize first and last
# character to each word
newSeries = series.map(lambda x: x[0].upper() + x[1:-1] + x[-1].upper())

# Print the resulting series
print("\nResulting Series :")
newSeries
