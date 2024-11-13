# Build the recommendation model using ALS on the training data
als = ALS(maxIter=5,
		regParam=0.01,
		userCol="user_id",
		itemCol="book_id",
		ratingCol="rating")

#Fitting the model on the train_data
model = als.fit(train_data)
