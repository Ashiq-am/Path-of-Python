#Traning and evaluating for user1 with our model trained with the help of training data
recommendations = model.transform(user1)

#Displaying the predictions of books for user1
recommendations.orderBy('prediction',ascending=False).show()
