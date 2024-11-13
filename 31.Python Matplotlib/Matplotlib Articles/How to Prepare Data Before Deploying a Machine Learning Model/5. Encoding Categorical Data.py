# CATEGORICAL DATA
from sklearn.preprocessing import LabelEncoder
le_x = LabelEncoder()
x['State'] = le_x.fit_transform(x['State'])
