df_recency = df.groupby(by='Customer Name',
						as_index=False)['Order Date'].max()
df_recency.columns = ['CustomerName', 'LastPurchaseDate']
recent_date = df_recency['LastPurchaseDate'].max()
df_recency['Recency'] = df_recency['LastPurchaseDate'].apply(
	lambda x: (recent_date - x).days)
df_recency.head()
