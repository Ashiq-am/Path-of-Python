# function to take the data as group and perform aggregation
def meanofTargets(group1):
    wt = group1['worst texture'].agg('mean')
    wa = group1['worst area'].agg('mean')
    group1['Mean worst teture'] = wt
    group1['Mean worst area'] = wa
    return group1


df2 = df1.groupby('target').apply(meanofTargets)
df2
