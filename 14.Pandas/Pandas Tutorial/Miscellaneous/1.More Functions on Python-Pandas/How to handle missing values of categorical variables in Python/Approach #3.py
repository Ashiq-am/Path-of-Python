# filling missing values
# with mean column values
df.fillna(df.median(), inplace=True)
df.head(10)
