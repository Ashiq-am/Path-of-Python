# import modules
import quandl
from datetime import datetime
import matplotlib.pyplot as plt

# initialize parameters
start = datetime(2015, 1, 1)
end = datetime(2020, 1, 1)

# get the data
df = quandl.get('NSE/OIL', start_date = start,
				end_date = end,
				authtoken = 'enter_your_api_key')

# display
plt.figure(figsize=(20,10))
plt.title('Opening Prices from {} to {}'.format(start, end))
plt.plot(df['Open'])
plt.show()
