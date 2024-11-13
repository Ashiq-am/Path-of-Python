# apply Decision Tree Classifier
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
dtc = DecisionTreeClassifier()
dtc.fit(X_train, y_train)

y_pred = dtc.predict(X_test)
y_pred

print(accuracy_score(y_test, y_pred))

# Tabulating the results
tempResults = pd.DataFrame({'Algorithm': ['Decision tree Classifier Method'],
							'Accuracy': [dtc_acc]})
results = pd.concat([results, tempResults])
results = results[['Algorithm', 'Accuracy']]
results
