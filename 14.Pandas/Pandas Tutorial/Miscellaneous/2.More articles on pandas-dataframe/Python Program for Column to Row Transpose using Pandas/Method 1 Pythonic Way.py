# Reading Data From the text
# file
data = pd.read_csv(r'GFG.txt')


# create new data frame with
# split value columns seperates
# data into three columns as per
# separator mentioned
new = data["name"].str.split("|",expand = True)

# making separate first name column
# from new data frame assign columnn
# values to dataframe new columns
# named as name*
data["Name1"] = new[0]
data["Name2"] = new[1]
data["Name3"] = new[2]

# Dropping old Name columns
data.drop(columns =["name"], inplace = True)

# create seperate dataframes with two
# columns id,name
d_name1 = data[['dept','Name1']]
d_name2 = data[['dept','Name2']]
d_name3 = data[['dept','Name3']]

# perform concat/unions operation for
# vertical merging of dataframes
union_df=pd.concat([d_name1,d_name2,d_name3],ignore_index=True)
union_df.fillna('',inplace=True)

# concatenate values of series into one
# series "name"
union_df['name'] = union_df['Name1'].astype(str)+union_df['Name2'].astype(str)+union_df['Name3'].astype(str)

# drop column names
union_df.drop(['Name1','Name2','Name3'],axis=1,inplace=True)

# drop rows having empty values
final_df=union_df[union_df['name']!='']

# sort the dataframe data by dept values
final_df.sort_values('dept')
