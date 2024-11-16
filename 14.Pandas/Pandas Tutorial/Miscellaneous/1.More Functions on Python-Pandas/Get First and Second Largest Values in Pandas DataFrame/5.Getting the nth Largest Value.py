n = 3  # For third highest value

# Get the nth largest value
nth_largest_value = df['Scores'].nlargest(n).iloc[-1]
print(f"{n}rd Largest Value:", nth_largest_value)
