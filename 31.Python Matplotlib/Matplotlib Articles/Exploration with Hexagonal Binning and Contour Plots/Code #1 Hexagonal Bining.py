x = data['SqFtTotLiving']
y = data['TaxAssessedValue']

fig = sns.jointplot(x, y, kind ="hex",
					color ="# 4CB391")

fig.fig.subplots_adjust(top = 0.85)

fig.set_axis_labels('Total Sq.Ft of Living Space',
					'Assessed Value for Tax Purposes')

fig.fig.suptitle('Tax Assessed vs. Total Living Space',
				size = 18);
