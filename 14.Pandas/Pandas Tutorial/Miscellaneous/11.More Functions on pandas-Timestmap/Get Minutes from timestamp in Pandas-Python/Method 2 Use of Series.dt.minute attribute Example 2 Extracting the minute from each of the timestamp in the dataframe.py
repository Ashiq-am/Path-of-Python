# extract minutes from time stamps and
# add them as a separate column
df['minutes_from_timestamps'] = df['time_stamps'].dt.minute

# view the updated dataframe
print(df)
