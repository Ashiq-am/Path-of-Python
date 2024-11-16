# plotting Close price and exponential
# moving averages of 30 days
# using .plot() method
reliance[['Close', 'EWMA30']].plot(label='RELIANCE',
								figsize=(16, 8))
