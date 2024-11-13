# Read only column A, B, C of all
# the four columns A,B,C,D in Sheet2
df=pd.read_excel('Sample1.xlsx',
				sheet_name = 1, usecols = 'A : C')
df.head()
