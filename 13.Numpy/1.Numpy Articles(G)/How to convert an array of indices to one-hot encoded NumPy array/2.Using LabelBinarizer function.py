import numpy as np
import sklearn.preprocessing
arr = np.array([4,7,2,9])
label_binarizer = sklearn.preprocessing.LabelBinarizer()
label_binarizer.fit(range(max(arr)+1))
encoded_arr = label_binarizer.transform(arr)
print('{0}'.format(encoded_arr))
