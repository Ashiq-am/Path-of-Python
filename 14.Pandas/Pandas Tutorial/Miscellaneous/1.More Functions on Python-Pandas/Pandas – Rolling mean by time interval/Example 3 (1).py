# calculating Rolling mean and storing it into
# a new column of existing dataFrame we have set
# the window as 200 and rest all parameters are
# set to default.
tesla_df['MA200'] = tesla_df['Close'].rolling(200).mean()

# Rolling mean is also called as Moving Average, hence
# we have used the notation MA and MA200 is the moving
# average (rolling mean) of 200 days

# printing dataframe
tesla_df
