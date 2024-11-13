tips = sns.load_dataset('tips')
sns.catplot(x='day',
			y='total_bill',
			data=tips,
			kind='box');
