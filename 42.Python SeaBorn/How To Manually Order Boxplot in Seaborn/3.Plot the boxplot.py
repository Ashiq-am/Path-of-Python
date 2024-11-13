# illustrate box plot
fx = sns.boxplot(x='day', y='total_bill', data=tips, hue='sex', palette='Set2')
