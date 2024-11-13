# Tabulating the results
tempResults = pd.DataFrame({'Algorithm': ['Support Vector Classifier Method'],
							'Accuracy': [svc_acc]})
results = pd.concat([results, tempResults])
results = results[['Algorithm', 'Accuracy']]
results
