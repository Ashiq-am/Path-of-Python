import yfinance as yf

try:
    data = yf.download("MSFT")
    print(data)
except Exception as e:
    print(f"Error: {e}")
