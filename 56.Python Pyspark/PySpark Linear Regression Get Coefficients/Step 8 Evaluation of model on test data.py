test_results = lrModel.evaluate(test_data)

#Printing Residuals which is the difference between the actua
#l value and the value predicted by the model (y-ŷ) for any given point
test_results.residuals.show(5)
