# Step 3: Initialize Cerebro and Add Strategy/Data

cerebro = bt.Cerebro()
cerebro.addstrategy(TestStrategy)
cerebro.adddata(data_bt)

# Run Backtrader
cerebro.run()