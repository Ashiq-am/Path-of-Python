# Select FRUITS name having PRICE <70
print(df.loc[df['PRICE'] < 70,
			['FRUITS', 'PRICE']])
