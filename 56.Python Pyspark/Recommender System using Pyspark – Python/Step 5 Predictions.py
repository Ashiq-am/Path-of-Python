# Evaluate the model by computing the RMSE on the test data
predictions = model.transform(test_data)

#Displaying predictions calculated by the model
predictions.show()
