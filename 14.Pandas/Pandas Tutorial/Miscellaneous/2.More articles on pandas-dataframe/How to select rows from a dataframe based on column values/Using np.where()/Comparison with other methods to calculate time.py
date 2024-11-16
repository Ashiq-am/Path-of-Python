# to calculate time
#%%timeit

li=['Albert','Louis','John']

# Pandas method only
df[(df.points>50)&(~df.name.isin(li))]
