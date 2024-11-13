from statsmodels.stats.power import TTestPower


power = TTestPower()
n_test = power.solve_power(nobs=40, effect_size = 0.5,
						power = None, alpha = 0.05)
print('Power: {:.3f}'.format(n_test))
