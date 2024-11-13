""
'''
# apply Support Vector Machine
from sklearn import svm

svc = svm.SVC()
svc.fit(X_train, y_train

y_pred = svc.predict(X_test) 
y_pred

from sklearn.metrics import accuracy_score

print(accuracy_score(y_test, y_pred))

'''
