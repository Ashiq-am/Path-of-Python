# import pandas module for data frame
import pandas as pd

# Create dataframe for student data in different colleges
subjectsdata = {'Name': ['sravan', 'sravan', 'sravan', 'sravan',
                         'sravan', 'sravan', 'sravan', 'sravan',
                         'Ojaswi', 'Ojaswi', 'Ojaswi', 'Ojaswi',
                         'Ojaswi', 'Ojaswi', 'Ojaswi', 'Ojaswi',
                         'Rohith', 'Rohith', 'Rohith', 'Rohith',
                         'Rohith', 'Rohith', 'Rohith', 'Rohith'],

                'college': ['VFSTRU', 'VFSTRU', 'VFSTRU', 'VFSTRU',
                            'VFSTRU', 'VFSTRU', 'VFSTRU', 'VFSTRU',
                            'VIT', 'VIT', 'VIT', 'VIT', 'VIT', 'VIT',
                            'VIT', 'VIT', 'IIT-Bhu', 'IIT-Bhu', 'IIT-Bhu',
                            'IIT-Bhu', 'IIT-Bhu', 'IIT-Bhu', 'IIT-Bhu',
                            'IIT-Bhu'],

                'subject': ['java', 'dbms', 'dms', 'coa', 'python', 'dld',
                            'android', 'iot', 'java', 'dbms', 'dms', 'coa',
                            'python', 'dld', 'android', 'iot', 'java',
                            'dbms', 'dms', 'coa', 'python', 'dld', 'android',
                            'iot']
                }

# Convert into data frame
df = pd.DataFrame(subjectsdata)

# print the data(student records)
print(df)
