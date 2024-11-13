# Target variables
y = np.where(df['Close'].shift(-1) > df['Close'], 1, 0)
y
