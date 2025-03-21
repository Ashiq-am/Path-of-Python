# import necessary packages
import pandas as pd
import matplotlib.pyplot as plt

# create a dataframe
stockValues = pd.DataFrame(
	{'Stock_Values': [60, 102, 103, 104, 101, 105,
					102, 103, 103, 102]})

# finding EMA
# com value=0.1 (0 approx)
ema = stockValues.ewm(com=0.1).mean()

# Comparision plot b/w stock values & EMA
plt.plot(stockValues, label="Stock Values", color="blue")
plt.plot(ema, label="EMA Values", color="green")
plt.xlabel("Days")
plt.ylabel("Price")
plt.legend()
plt.show()
