Data_list = ["Emp Name","Date of Birth",
			" Gender-m/f","Paid salary"]

new_df = df.toDF(*Data_list)
new_df.show()
