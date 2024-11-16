# Latest timestamp
print("Latest Timestamp: ", max(df['new_time']))

# Get difference between 2 timestamps
diff = abs(df['new_time'][0]-df['new_time'][1])
print("Difference: ", diff)
