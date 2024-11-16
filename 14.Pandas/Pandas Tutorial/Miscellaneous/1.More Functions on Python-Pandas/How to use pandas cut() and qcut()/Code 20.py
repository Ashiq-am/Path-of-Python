# basically dividing data into 3
# quantiles
pd.qcut(df.Kms_Driven,
		q=np.linspace(0,1,4)).head()
