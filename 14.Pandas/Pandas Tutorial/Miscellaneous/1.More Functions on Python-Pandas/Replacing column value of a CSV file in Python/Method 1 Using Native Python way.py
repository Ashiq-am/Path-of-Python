# reading the CSV file
text = open("csvfile.csv", "r")

#join() method combines all contents of
# csvfile.csv and formed as a string
text = ''.join([i for i in text])

# search and replace the contents
text = text.replace("EmployeeName", "EmpName")
text = text.replace("EmployeeNumber", "EmpNumber")
text = text.replace("EmployeeDepartment", "EmpDepartment")
text = text.replace("lined", "linked")

# output.csv is the output file opened in write mode
x = open("output.csv","w")

# all the replaced text is written in the output.csv file
x.writelines(text)
x.close()
