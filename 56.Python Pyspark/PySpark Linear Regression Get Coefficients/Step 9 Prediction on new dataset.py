unlabeled_data = test_data.select('features')

predictions = lrModel.transform(unlabeled_data)
predictions.show(5)
