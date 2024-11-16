# there is no use of DateTime module
# so remove it
train = train.drop(['DateTime'], axis=1)

# seperating class label for training the data
train1 = train.drop(['Vehicles'], axis=1)

# class label is stored in target
target = train['Vehicles']

print(train1.head())
target.head()
