from scipy import stats

sales_with_chipotle = [13.4, 10.9, 11.2, 11.8,
					14, 15.3, 14.2, 12.6,
					17, 16.2, 16.5, 15.7]

sales_without_chipotle = [12, 11.7, 10.7, 11.2,
						14.8, 14.4, 13.9, 13.7,
						16.9, 16, 15.6, 16]

t_value, p_value = stats.ttest_ind(sales_with_chipotle,
								sales_without_chipotle)

print('Test statistic is %f' % float("{:.6f}".format(t_value)))
print('p-value for two tailed test is %f' % p_value)

alpha = 0.05
if p_value <= alpha:

	print('Conclusion', 'n', 'Since p-value(=%f)' % p_value,
		'<', 'alpha(=%.2f)' % alpha,
		'''We reject the null hypothesis H0. \
		So we conclude that the \
		Mean sales is affected by \
		adding chipotle sauce to the best\
		selling ingredient i.e., μ1 = μ2 at \
		%.2f level of significance.''' % alpha)

else:

	print('Conclusion', 'n', 'Since p-value(=%f)' % p_value,
		'>', 'alpha(=%.2f)' % alpha,
		'We fail to reject the null \
		hypothesis H0, which signifies \
		the Mean of sales is not affected\
		by adding chioptle sauce.')
