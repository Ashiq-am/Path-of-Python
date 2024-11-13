import numpy as np
import talib

# Generate random closing prices
close_prices = np.random.random(100)
# Calculate the 20-period SMA
sma = talib.SMA(close_prices, timeperiod=20)
print(sma)
