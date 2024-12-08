import backtrader as bt
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime

# Step 1: Generate Synthetic Data for Backtrader

np.random.seed(0)
days = 100
start_date = datetime.datetime(2020, 1, 1)
date_range = pd.date_range(start=start_date, periods=days)
price = 100 + np.cumsum(np.random.randn(days) * 2)
data = pd.DataFrame({'datetime': date_range, 'open': price, 'high': price + np.random.rand(days) * 2,
'low': price - np.random.rand(days) * 2, 'close': price, 'volume': np.random.randint(100, 500, days)})
data.set_index('datetime', inplace=True)
data_bt = bt.feeds.PandasData(dataname=data)