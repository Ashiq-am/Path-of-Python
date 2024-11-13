df['diagnosis'] = df['diagnosis'].map({'M': 1, 'B': 0})
df.head()

df['diagnosis'].unique()

X = df.drop('diagnosis', axis=1)
X.head()

y = df['diagnosis']
y.head()
