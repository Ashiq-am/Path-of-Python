# defining the lambda function as 'score'
score = (lambda x : (x / x.mean()))

# applying transform() on all the
# columns of DataFrame inside the
# transform(), passing the score
df_tra = df.groupby(level=["region"]).transform(score)
print(df_tra.head(10))
