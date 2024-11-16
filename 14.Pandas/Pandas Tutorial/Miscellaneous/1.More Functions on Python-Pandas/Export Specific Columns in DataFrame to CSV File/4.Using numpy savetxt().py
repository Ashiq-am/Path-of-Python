import numpy as np
desired_columns = df[['Age','Education','Salary']]
np.savetxt(
	"output.csv",
	desired_columns,
	delimiter=',',
	header=','.join(desired_columns),
	fmt='%s', # to convert all datatypes to strings
	comments='' # this part is necessary to avoid necessary comments like #
)
