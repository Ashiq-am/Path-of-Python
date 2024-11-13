# apply Rnadom Forest Classifier
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier()
rfc.fit(X_train, y_train)

y_pred = rfc.predict(X_test)
y_pred

print(accuracy_score(y_test, y_pred))

# tabulating the results
tempResults = pd.DataFrame({'Algorithm': ['Random Forest Classifier Method'],
							'Accuracy': [rfc_acc]})

results = pd.concat([results, tempResults])
results = results[['Algorithm', 'Accuracy']]
results
