# importing pandas
import pandas as pd

file_list=['a.csv','b.csv','c.csv']

main_dataframe = pd.DataFrame(pd.read_csv(file_list[0]))

for i in range(1,len(file_list)):
	data = pd.read_csv(file_list[i])
	df = pd.DataFrame(data)
	main_dataframe = pd.concat([main_dataframe,df],axis=1)
print(main_dataframe)
