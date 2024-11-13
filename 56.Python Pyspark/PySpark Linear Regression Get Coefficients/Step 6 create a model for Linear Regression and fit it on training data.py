from pyspark.ml.regression import LinearRegression

# Create a Linear Regression Model object
lr = LinearRegression(labelCol='Yearly Amount Spent')

# Fit the model to the data and call this model lrModel
lrModel = lr.fit(train_data)
lrModel
