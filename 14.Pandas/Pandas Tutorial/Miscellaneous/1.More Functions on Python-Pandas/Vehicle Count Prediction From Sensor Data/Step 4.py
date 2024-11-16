#importing Random forest
from sklearn.ensemble import RandomForestRegressor

#defining the RandomForestRegressor
m1=RandomForestRegressor()

m1.fit(train1,target)
#testing
m1.predict([[11,6,0,1,2015,11,2]])
