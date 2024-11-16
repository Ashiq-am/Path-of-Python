df['Yr_qcut'] = pd.qcut(df.Year, q=5,
						labels=['oldest',
								'not so old',
								'medium',
								'newer',
								'latest'])
df.head()

df['Yr_qcut'].value_counts().plot(kind='barh')
plt.show()

qcut_series, qcut_intervals = pd.qcut(df.Year, q=5,
									labels=['oldest',
											'not so old',
											'medium',
											'newer',
											'latest'],
									retbins=True)

qcut_series.value_counts()
