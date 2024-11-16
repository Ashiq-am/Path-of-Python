# Create a pipeline that applies both the functions created above
pipeline = df.pipe(mean_age_by_group, col='gender').pipe(uppercase_column_name)

# calling pipeline
pipeline
