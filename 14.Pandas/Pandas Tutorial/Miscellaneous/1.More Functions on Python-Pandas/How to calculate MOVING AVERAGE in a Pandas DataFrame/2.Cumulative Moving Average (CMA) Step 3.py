# updating our dataFrame to have only
# one column 'Close' as rest all columns
# are of no use for us at the moment
# using .to_frame() to convert pandas series
# into dataframe.
reliance = reliance['Close'].to_frame()

# calculating cumulative moving
# average using .expanding().mean()
reliance['CMA30'] = reliance['Close'].expanding().mean()

# printing Dataframe
reliance
