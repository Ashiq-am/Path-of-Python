# filling missing values
# with mean column values
df.fillna(df.mode(), inplace=True)
df.sample(10)
