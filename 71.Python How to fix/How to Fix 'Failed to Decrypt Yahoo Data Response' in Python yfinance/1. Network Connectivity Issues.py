import yfinance as yf

try:
    data = yf.download("GOOG")
    print(data)
except Exception as e:
    print(f"Error: {e}")
