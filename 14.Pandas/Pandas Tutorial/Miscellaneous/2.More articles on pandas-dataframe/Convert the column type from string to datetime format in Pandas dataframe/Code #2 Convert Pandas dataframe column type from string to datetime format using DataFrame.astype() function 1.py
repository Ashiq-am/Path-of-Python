# convert the 'Date' column to datetime format
df['Date'] = df['Date'].astype('datetime64[ns]')

# Check the format of 'Date' column
df.info()
