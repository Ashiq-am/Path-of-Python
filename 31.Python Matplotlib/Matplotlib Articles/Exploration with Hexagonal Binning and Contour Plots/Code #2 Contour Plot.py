fig2 = sns.kdeplot(x, y, legend = True)

plt.xlabel('Total Sq.Ft of Space')

plt.ylabel('Assessed Value for Taxes')

fig2.figure.suptitle('Tax Assessed vs. Total Living', size = 16);
