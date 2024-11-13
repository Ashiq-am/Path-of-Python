Id_list = [1, 2]
college_list = ['DU','IIT']
dataframe.filter((dataframe.student_ID.isin(Id_list)) |
				(dataframe.college.isin(college_list))).show()
