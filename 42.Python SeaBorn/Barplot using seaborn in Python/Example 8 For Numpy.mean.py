from numpy import mean
sns.barplot(x = 'class', y = 'fare', hue = 'sex', data = df, estimator=mean)
