# Updating the dataFrame with just the
# column 'Close' as others columns are
# of no use right now we have used .to_frame
# which converts Series to a DataFrame.
tesla_df = tesla_df['Close'].to_frame()


# calculating Rolling mean and storing it
# into a new column of existing dataFrame
# we have set the window as 30 and rest all
# parameters are set to default.
tesla_df['MA30'] = tesla_df['Close'].rolling(30).mean()

# Rolling mean is also called as Moving Average ,
# hence we have used the notation MA
# and MA30 is the moving average (rolling mean)
# of 30 days

# printing dataframe
tesla_df
