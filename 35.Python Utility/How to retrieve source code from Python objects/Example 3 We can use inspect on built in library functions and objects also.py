# import inspect library
import inspect
import pandas


source_DF = inspect.getsource(pandas.DataFrame)
print(source_DF[:100])
