model = ols('conformity ~ C(fcategory) * C(partner_status)', data=data).fit()
anova_table = sm.stats.anova_lm(model, typ=2)
print(anova_table)
