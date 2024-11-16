from turtle import pd

from pandas import np

df = pd.DataFrame(np.random.randn(1000, 2), columns =['a', 'b'])
df.plot.hexbin(x ='a', y ='b', gridsize = 25, cmap ='Oranges')
