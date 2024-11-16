# Get the second highest value
second_highest_value = df['Scores'].nlargest(2).iloc[-1]
print("Second Highest Value:", second_highest_value)
