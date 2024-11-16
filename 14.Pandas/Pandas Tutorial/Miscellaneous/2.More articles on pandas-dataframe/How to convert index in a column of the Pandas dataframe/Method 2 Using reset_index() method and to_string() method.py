# CREATING A DATAFRAME FOR STUDENTS PORTFOLIO

# importing the pandas library as pd
import pandas as pd

# Creating the dataframe Ab
AB = pd.DataFrame({'Roll Number': ['9917102206', '9917102250', '9917102203', '9917102204', '9917102231'],
                   'Name': ['TANYA', 'PREETIKA', 'KUSHAGRA', 'PRAKHAR', 'ASHISH'],
                   'Score': [99, 98, 50, 45, 97],
                   'Grade': ['A+', 'A+', 'C+', 'C', 'A'],
                   'Subject': ['Operating Systems', 'Operating Systems', 'Operating Systems', 'Operating Systems',
                               'Operating Systems']})

# importing the pandas library as pd
import pandas as pd

# Creating the dataframe Ab
AB = pd.DataFrame({'Roll Number': ['9917102206', '9917102250',
                                   '9917102203', '9917102204',
                                   '9917102231'],
                   'Name': ['TANYA', 'PREETIKA', 'KUSHAGRA',
                            'PRAKHAR', 'ASHISH'],
                   'Score': [99, 98, 50, 45, 97],
                   'Grade': ['A+', 'A+', 'C+', 'C', 'A'],
                   'Subject': ['Operating Systems', 'Operating Systems',
                               'Operating Systems', 'Operating Systems',
                               'Operating Systems']})

# USING RESET_INDEX METHOD
# Adding a new index column to AB dataframe
AB.reset_index(level=0, inplace=True)

# HIDING THE DEFAULT INDEX VALUES AND
# PRINTING DATAFRAME
print(AB.to_string(index=False))
