# convert the 'Date' column to datetime format
df['Date']= pd.to_datetime(df['Date'])

# Check the format of 'Date' column
df.info()
