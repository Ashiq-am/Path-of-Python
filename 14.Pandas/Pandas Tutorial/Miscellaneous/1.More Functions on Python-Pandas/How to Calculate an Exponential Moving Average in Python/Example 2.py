# import necessary packages
import pandas as pd
import matplotlib.pyplot as plt

# create a dataframe
stockValues = pd.DataFrame(
	{'Stock_Values': [60, 102, 103, 104, 101, 105,
					102, 103, 103, 102]})

# finding EMA
# used constant value as 0.8
ema = stockValues.ewm(com=0.8).mean()

# Comparision plot b/w stock values & EMA
plt.plot(stockValues, label="Stock Values", color="black")
plt.plot(ema, label="EMA Values", color="red")
plt.xlabel("Days")
plt.ylabel("Price")
plt.legend()
plt.show()
