# importing packages
import pandas as pd
import glob

folder_path = 'Path_of_file/csv_files'
file_list = glob.glob(folder_path + "/*.csv")
main_dataframe = pd.DataFrame(pd.read_csv(file_list[0]))
for i in range(1,len(file_list)):
	data = pd.read_csv(file_list[i])
	df = pd.DataFrame(data)
	main_dataframe = pd.concat([main_dataframe,df],axis=1)
print(main_dataframe)
