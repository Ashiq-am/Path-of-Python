import yfinance as yf

try
    data = yf.download("AAPL")
    print(data)
except Exception as e:
    print(f"Error: {e}")
