# filling missing values
# with mean column values
df.fillna(df.mean(), inplace=True)
df.sample(10)
