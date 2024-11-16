# IQR
Q1 = np.percentile(df_boston['DIS'], 25,
				interpolation = 'midpoint')

Q3 = np.percentile(df_boston['DIS'], 75,
				interpolation = 'midpoint')
IQR = Q3 - Q1
