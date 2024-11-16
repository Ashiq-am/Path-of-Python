# Reset index to use MultiIndex
combined_data.reset_index(inplace=True)

# Set MultiIndex
combined_data.set_index(['Date', 'Ticker'], inplace=True)
print(combined_data)
