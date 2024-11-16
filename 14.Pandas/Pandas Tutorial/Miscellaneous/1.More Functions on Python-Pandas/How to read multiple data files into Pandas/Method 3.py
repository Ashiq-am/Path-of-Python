# importing packages
import pandas as pd
import glob

folder_path = 'Path_/files'
file_list = glob.glob(folder_path + "/*.txt")
main_dataframe = pd.DataFrame(pd.read_table(file_list[0]))

for i in range(1,len(file_list)):
	data = pd.read_table(file_list[i])
	df = pd.DataFrame(data)
	main_dataframe = pd.concat([main_dataframe, df], axis = 1)

print(main_dataframe)

# creating a new csv file with
# the dataframe we created
main_dataframe.to_csv('new_csv1.csv')
