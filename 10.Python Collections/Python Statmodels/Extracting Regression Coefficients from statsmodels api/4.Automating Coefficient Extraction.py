def get_coef_table(lin_reg):
    coef_df = pd.DataFrame({
        'coef': lin_reg.params.values,
        'pvalue': lin_reg.pvalues.round(4),
        'ci_lower': lin_reg.conf_int()[0],
        'ci_upper': lin_reg.conf_int()[1]
    }, index=lin_reg.params.index)
    return coef_df

coef_table = get_coef_table(results)
print(coef_table)
