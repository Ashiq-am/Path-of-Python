import pandas as pd
# pd.read_csv creates dataframes
df1 = pd.read_csv('D:\python\data_files\data_files\emp_1.txt')
df2 = pd.read_csv('D:\python\data_files\data_files\emp_2.txt')
df3 = pd.read_csv('D:\python\data_files\data_files\emp_3.txt')

frames = [df1, df2, df3]

# concat function concatenates the frames
result = pd.concat(frames)
# to_csv function writes output to file
result.to_csv('D:\\python\\data_files'
			'\\target_file\\master.txt', encoding ='utf-8', index = False)
