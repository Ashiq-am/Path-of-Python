lis = ['CreditScore', 'Age', 'Balance', 'EstimatedSalary']
plt.subplots(figsize=(15, 8))
index = 1

for i in lis:
	plt.subplot(2, 2, index)
	sns.distplot(dataset[i])
	index += 1
