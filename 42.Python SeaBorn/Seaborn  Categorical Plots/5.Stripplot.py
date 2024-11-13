sns.stripplot(x ='day', y ='total_bill', data = df,
			jitter = True, hue ='smoker', dodge = True)
