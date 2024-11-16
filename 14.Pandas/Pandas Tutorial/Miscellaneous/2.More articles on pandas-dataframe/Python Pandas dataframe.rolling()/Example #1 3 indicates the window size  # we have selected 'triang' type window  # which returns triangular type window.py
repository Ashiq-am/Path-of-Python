# 3 indicates the window size
# we have selected 'triang' type window
# which returns triangular type window

# sum() function find the sum over
# all the windows in our data frame
df.close.rolling(3, win_type ='triang').sum()
