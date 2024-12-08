# Step 2: Define a Simple Backtrader Strategy

class TestStrategy(bt.Strategy):
    def next(self):
        self.log(f"Close: {self.data.close[0]}")

def log(self, txt, dt=None):
    dt = dt or self.datas[0].datetime.date(0)
    print(f"{dt.isoformat()}, {txt}")